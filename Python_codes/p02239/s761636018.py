from collections import deque
from enum import Enum

class Bfs(object):
    """ Breadth First Search """
    class Status(Enum):
        """ ?????????????¨??????¶??? """
        white = 1  # ????¨????
        gray = 2  # ?¨???????
        black = 3  #?¨???????

    def __init__(self, data):
        num_of_nodes = len(data)+1
        self.color = [Bfs.Status.white] * (num_of_nodes + 1)  # ????????????????¨??????¶???
        self.Q = deque()  # ?¨???????????????????????????¨????????\???
        self.M = self._make_matrix(data)  # data????????????????????£??\??????
        self.D = [-1] * (len(data) + 1)  # ????????????????????¢ (-1????????????????????°????????????)

    def _make_matrix(self, data):
        """ data(??£??\?????????)???????????£??\??????????????? (M[i][j]?????¢??§??????????????????+1??????????????????????????????) """
        num = len(data)
        graph_table = [[0] * (num+1) for _ in range(num+1)]
        for d in data:
            node_id = d[0]
            num_of_e = d[1]
            for e in d[2:]:
                graph_table[node_id][e] = 1
        return graph_table

    def search(self, start):
        """ start????????????????????????????????°??????????????? """
        self.Q.append(start)
        self.color[start] = Bfs.Status.gray
        self.D[start] = 0  # ???????????§????????¢???0

        while self.Q:
            u = self.Q.popleft()  # ?????¨?¨????????????????????????°??????
            edges = self.M[u]
            for i in range(1, len(edges)):
                if edges[i] == 1 and self.color[i] == Bfs.Status.white:
                    self.color[i] = Bfs.Status.gray
                    if self.D[i] == -1:
                        self.D[i] = self.D[u] + 1
                        self.Q.append(i)  # ?¨??????????????????????????¬??????????????????? ???????????????????????????self.S[-1]?????????????????????


if __name__ == '__main__':
    # ??????????????\???
    num = int(input())
    data = []
    for _ in range(num):
        data.append(list(map(int, input().split(' '))))

    # ???????????????
    # data[]????????????????????????1?????????????????£??\?????????????????????????´?????????????????????¨????????????????????????(??´???????????£??????????????????????????????)
    d = Bfs(data)
    d.search(1)

    # ???????????????
    for i in range(1, num+1):
        print('{0} {1}'.format(i, d.D[i]))
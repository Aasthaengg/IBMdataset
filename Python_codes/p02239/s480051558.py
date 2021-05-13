from collections import deque


def get_next_node(node, discovery_time, adj_mat):
    for i, node in enumerate(adj_mat[node]):
        if discovery_time[i] == 0 and node == 1:
            return i
    return None

def bfs(node, adj_mat):
    distances = [-1] * len(adj_mat)

    distances[node] = 0
    q = deque(maxlen=len(adj_mat))
    q.append(0)
    while q:
        visit_node = q.popleft()
        for j in range(len(adj_mat)):
            if adj_mat[visit_node][j] and distances[j]==-1:
                distances[j] = distances[visit_node] + 1
                q.append(j)
    
    for i, d in enumerate(distances):
        print(i+1, d)


if __name__ == "__main__":
    n_node = int(input())
    # f = open('alds1_11_c-input.txt', 'r')
    # n_node = int(f.readline())

    adjacency_mat = [[0 for i in range(n_node)] for j in range(n_node)]
    for i in range(n_node):
        command = list(map(int, input().split()))
        # command = list(map(int, f.readline().split()))

        i = command.pop(0) - 1
        n_edge = command.pop(0)

        for j in command:
            adjacency_mat[i][j-1] = 1

    # f.close()
    discovery_time = [0] * n_node
    finish_time = [0] * n_node
    bfs(0, adjacency_mat)

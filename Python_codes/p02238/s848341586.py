# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_B
# Depth First Search
# Result:
import sys

class Graph(object):
    def __init__(self, size):
        super(Graph, self).__init__()
        self.__size = size
        self.__vertices = [None] * size

    def add_vertex(self, vertex):
        self.__vertices[vertex.id_ - 1] = vertex

    def get_vertex(self, vid):
        return self.__vertices[vid - 1]

    def depth_first_search(self):
        d = [0] * self.__size
        f = [0] * self.__size
        timer = 1
        for j in range(1, self.__size + 1):
            vtx = self.get_vertex(j)
            if not vtx.visited:
                stack = [vtx]
                d[vtx.id_ - 1] = timer
                vtx.visited = True
                timer = self.__depth_first_search(stack, timer, d, f) + 1

        for vtx in self.__vertices:
            print '%d %d %d' % (vtx.id_, d[vtx.id_ - 1], f[vtx.id_ - 1])

    def __depth_first_search(self, stack, timer, d, f):
        while len(stack) > 0:
            top = stack[-1]
            avid = top.get_next_adjacnt()
            if avid == -1:
                timer += 1
                f[top.id_ - 1] = timer
                stack.pop()
            else:
                av = self.get_vertex(avid)
                if not av.visited:
                    timer += 1
                    stack.append(av)
                    d[av.id_ - 1] = timer
                    av.visited = True
        return timer

    def __str__(self):
        str_ = ''
        for e in self.__vertices:
            str_ += '%s\n' % e
        return str_

class Vertex(object):
    def __init__(self, id_):
        super(Vertex, self).__init__()
        self.id_ = id_
        self.adjacents = []
        self.next_idx = 0
        self.visited = False

    def add_adjacent(self, avid):
        self.adjacents.append(avid)

    def get_next_adjacnt(self):
        if len(self.adjacents) == 0: return -1
        if self.next_idx < len(self.adjacents):
            val = self.adjacents[self.next_idx]
            self.next_idx += 1
            return val
        else:
            return -1

    def __str__(self):
        str_ = '%d ' % self.id_
        if len(self.adjacents) == 0:
            str_ += '0'
        else:
            str_ += '%d' % len(self.adjacents)
            for e in self.adjacents:
                str_ += ' %d' % e
        return str_



s = int(sys.stdin.readline().strip())
graph = Graph(s)
for _ in range(0, s):
    vals = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    v = Vertex(vals[0])
    graph.add_vertex(v)
    if vals[1] == 0: continue
    for i in range(0, vals[1]):
        v.add_adjacent(vals[2 + i])

graph.depth_first_search()
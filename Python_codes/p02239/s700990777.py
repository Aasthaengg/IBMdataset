# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_C
# Breadth First Search
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

    def breadth_first_search(self):
        ds = [-1] * self.__size
        vs = [None] * self.__size
        vs[0] = [self.get_vertex(1)]
        ds[0] = 0
        vs_idx = 0
        while vs_idx < self.__size and vs[vs_idx] != None:
            vlst = vs[vs_idx]
            vs_idx += 1
            for vtx in vlst:
                for advid in vtx.adjacents:
                    adv = self.get_vertex(advid)
                    if ds[advid - 1] == -1:
                        ds[advid - 1] = vs_idx
                        if vs[vs_idx] == None:
                            vs[vs_idx] = []
                        vs[vs_idx].append(adv)
        for idx, d in enumerate(ds):
            print '%d %d' % ((idx + 1), d)

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

    def add_adjacent(self, avid):
        self.adjacents.append(avid)

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

graph.breadth_first_search()
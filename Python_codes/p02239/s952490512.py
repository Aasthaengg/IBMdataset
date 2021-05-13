from sys import stdin

def bfs(graph,start,d):
    queue = [start]
    explored = []

    while len(queue) > 0:
        node = queue.pop(0)
#        print 'node ' + str(node)
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                if neighbour not in queue:
                    # print 'neighbour ' + str(neighbour)
                    if d[neighbour-1] == -1:
                        d[neighbour - 1] = d[node - 1] + 1
                        queue.append(neighbour)
                        # print 'queue ' + str(queue)

            explored.append(node)

        # print 'd ' + str(d)
        # print '\n'


def main():
    n = int(stdin.readline())

    graph_dict = {}

    d = [-1]*n

    for i in xrange(n):
        entry = [int(s) for s in stdin.readline().split()[2:]]
        graph_dict[i+1] = entry

    d[0] = 0
    bfs(graph_dict,1,d)

    for i in xrange(n):
        print str(i+1) + ' ' + str(d[i])

main()

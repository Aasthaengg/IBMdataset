import sys
sys.setrecursionlimit(10**9)

N, M = map(int, input().split())

paths = [[] for i in range(N)]
longest_paths = [-1 for i in range(N)]

for i in range(M):
    x, y = map(int, input().split())
    paths[x-1].append(y-1)

def get_longest(node):
    if longest_paths[node] != -1:
        return longest_paths[node]
    if paths[node] == []:
        longest_paths[node] = 0
        return 0
    else:
        result = max([get_longest(nd) for nd in paths[node]]) + 1
        longest_paths[node] = result
        return result

print(max([get_longest(i) for i in range(N)]))
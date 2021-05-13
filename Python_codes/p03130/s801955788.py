''' Hey stalker :) '''
INF = 10**10
def main():
    print = out.append
    ''' Cook your dish here! '''
    adj = [[] for _ in range(4)]
    visited = [False]*4
    for _ in range(3):
        x, y = get_list()
        adj[x-1].append(y-1)
        adj[y-1].append(x-1)
    def dfs(root):
        #print(root)
        visited[root] = True
        for v in adj[root]:
            if not visited[v]:
                dfs(v)
                return
    dfs(0)
    print("YES") if False not in visited else print("NO")


''' Pythonista fLite 1.1 '''
import sys
from collections import defaultdict, Counter
from bisect import bisect_left, bisect_right
#from functools import reduce
import math
#input = iter(sys.stdin.buffer.read().decode().splitlines()).__next__
out = []
get_int = lambda: int(input())
get_list = lambda: list(map(int, input().split()))
main()
#[main() for _ in range(int(input()))]
print(*out, sep='\n')

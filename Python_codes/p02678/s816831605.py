import sys


# import math
import heapq

# input = sys.stdin.readline
from collections import deque

def main():
    n, m = map(int,input().split())
    room =[[]for _ in range(n+1)]
    for i in range(m):
        a,b = map(int,input().split())
        room[a].append(b)
        room[b].append(a)

    point = [0] *(n+1) #未踏0 その他　親
    d = deque([1])

    while len(d) > 0:
        p = d.popleft()
        for v in room[p]:
            if point[v] ==0:
                d.append(v)
                point[v] =p

    if 0 in point[1:]:
        print('No')
    else:
        print("Yes")
        print("\n".join(map(str,point[2:])))












if __name__ == "__main__":
    main()

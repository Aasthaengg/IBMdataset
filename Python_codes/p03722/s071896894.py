import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    INF = 10**18
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]

    N,M = LI()
    root = []
    for _ in range(M):
        a,b,c = LI()
        root.append((a-1,b-1,c))
    node = [-INF]* N

    node[0] = 0
    up = False
    for _ in range(N):
        up = False
        for a,b,c in root:
            if node[a] + c > node[b]:
                node[b] = node[a] + c
                if b == N-1: up = True
    if up:
        print('inf')
    else:
        print(node[N-1])


if __name__ == '__main__':
    main()
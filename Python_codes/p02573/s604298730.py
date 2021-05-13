import sys
sys.setrecursionlimit(10**9)


N, M = map(int, input().split())
to = [[] for _ in range(N)]
count = 0

for _ in range(M):
    A, B = map(lambda x:int(x) - 1, input().split())
    to[A].append(B)
    to[B].append(A)


def dfs(v, to, seen):
    global count
    seen[v] = True
    count += 1
    for nv in to[v]:
        if seen[nv]:
            continue
        dfs(nv, to, seen)


def main():
    global count
    seen = [False] * N
    cnts = []
    for i in range(N):
        if not seen[i]:
            dfs(i, to, seen)
            cnts.append(count)
            count = 0
    
    print(max(cnts))


if __name__ == "__main__":
    main()


import sys
input = sys.stdin.buffer.readline


N = int(input())
A = [list(map(int, input().split()))[::-1] for _ in range(N)]
day = 0
cnt = N
Last = set([i for i in range(N)])
while cnt:
    flag = True
    Done = [False] * N
    L = set()
    for i in Last:
        if len(A[i]) == 0:
            continue
        if Done[i]:
            continue
        x = A[i][-1] - 1
        if A[x] and (not Done[x]) and (A[x][-1] - 1 == i):
            A[i].pop()
            A[x].pop()
            Done[i] = True
            Done[x] = True
            L.add(i)
            L.add(x)
            flag = False
            if not A[i]:
                cnt -= 1
            if not A[x]:
                cnt -= 1
    Last = L
    if flag:
        break
    day += 1
if cnt:
    print(-1)
else:
    print(day)
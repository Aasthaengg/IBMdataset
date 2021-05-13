N = int(input())
A = [int(input()) for _ in range(N)]
now = 1
c = 0
p = set([1])
while True:
    if A[now-1] in p:
        print(-1)
        exit()
    p.add(A[now-1])
    c += 1
    if A[now-1] == 2:
        break
    now = A[now-1]
print(c)

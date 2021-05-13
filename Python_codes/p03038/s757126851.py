from operator import itemgetter

n, m = map(int, input().split())
A = list(map(int, input().split()))
BC = [list(map(int, input().split())) for _ in range(m)]


BC.sort(reverse=True, key=itemgetter(1))
cnt = 0
for b, c in BC:
    if cnt + b > n:
        b = n-cnt
    for _ in range(b):
        A.append(c)
    cnt += b
    if cnt == n:
        break

A.sort(reverse=True)

print(sum(A[:n]))
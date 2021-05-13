from itertools import accumulate
n = int(input())
A = list(map(int, input().split()))
Acum = list(accumulate(reversed(A)))
Acum.reverse()

flexibility = 1
ans = 0
for i, a in enumerate(A):
    if flexibility < a:
        print(-1)
        exit()
    ans += min(flexibility, Acum[i])
    flexibility = 2*(flexibility-a)

print(ans)

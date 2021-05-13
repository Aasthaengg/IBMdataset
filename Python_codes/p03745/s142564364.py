N = int(input())
A = list(map(int, input().split()))
now = A[0]
kind = 0
ans = 0
for i in range(1,N):
    if kind == 0:
        if now < A[i]:
            kind = 1
        elif now > A[i]:
            kind = 2
    elif kind == 1: # 増加
        if now > A[i]:
            ans += 1
            kind = 0
    else: # 減少
        if now < A[i]:
            ans += 1
            kind = 0
    now = A[i]
print(ans+1)

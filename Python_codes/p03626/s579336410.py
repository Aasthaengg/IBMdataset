import sys
def I(): return int(sys.stdin.readline().rstrip())
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

N = I()
S1 = LS2()
S2 = LS2()
mod = 10**9+7

A = []
a = 0
while a < N:
    if S1[a] == S2[a]:
        a += 1
        A.append(1)
    else:
        a += 2
        A.append(2)

ans = 1
for i in range(len(A)):
    if i == 0:
        if A[i] == 1:
            ans *= 3
        else:
            ans *= 6
    else:
        if A[i] == 1 and A[i-1] == 1:
            ans *= 2
        if A[i] == 2 and A[i-1] == 1:
            ans *= 2
        if A[i] == 2 and A[i-1] == 2:
            ans *= 3
        ans %= mod

print(ans)
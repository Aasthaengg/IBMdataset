N = int(input())
if N == 1:print(1);exit()
A = [int(hoge) for hoge in input().split()]
ans = 1
cur = A[0]
Decided = A[0] != A[1]
Flat = A[0] == A[1]
Up = A[0] < A[1]

for n in range(1,N):
    if Decided:
        if A[n] == cur:
            continue
        if (A[n]>=cur) == Up:#数列が続く
            cur = A[n]
        else:
            cur = A[n]
            Up = 1 - Up
            Decided = False
            ans += 1
    else:
        if A[n] != cur:
            Up = A[n] > cur
            cur = A[n]
            Decided = True
print(ans) 
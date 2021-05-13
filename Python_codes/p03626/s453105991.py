import sys
input = sys.stdin.readline

N = int(input())
S, _ = input()+'_', input()

A = []

i=0
while i<N:
    if S[i]!=S[i+1]:
        A.append(1)
        i+=1
    else:
        A.append(2)
        i+=2

p = A[0]
ans = 3 if p==1 else 6
mod = 10**9+7
for a in A[1:]:
    d = 2 if p==1 else (1 if a==1 else 3)
    ans = (ans*d)%mod
    p = a

print(ans)
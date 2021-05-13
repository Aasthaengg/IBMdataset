N=int(input())
A=list(map(int,input().split(' ')))
ans = 0
for n,i in enumerate(A):
    if A[i-1]==n+1:
        ans += 1
print(ans//2)
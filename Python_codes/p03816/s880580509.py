N = int(input())
A = list(map(int,input().split()))

A_set = set(A)
ans=len(A_set)
if ans%2==0:
    ans-=1
print(ans)
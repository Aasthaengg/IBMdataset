n=int(input())
A=list(map(int,input().split()))
flag=True
if n%2==0:
    if 0 in A or len(set(A))!=n//2:flag=False
else:
    if A.count(0)!=1 or len(set(A))!=(n+1)//2:
        flag=False
if flag:
    print(2**(n//2)%(10**9+7))
else:
    print(0)
N=int(input())
A=list(map(int,input().split()))
oddcount=0
for i in range(N):
    if A[i]%2==1:
        oddcount=oddcount+1
if oddcount%2==1:
    print("NO")
else:
    print("YES")
n = int(input())
m=list(map(int,input().split()))
k=1
for i in range(n):
    if m[i]==k:
        k+=1
if k==1:
    print(-1)
else:
    
    print(n-k+1)
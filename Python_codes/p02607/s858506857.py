n=int(input())
a=list(map(int,input().split()))
cnt=0
for i in range(1,n+1,2):
    if a[i-1]%2: cnt+=1
print(cnt)
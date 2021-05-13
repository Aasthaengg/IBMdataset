n=int(input())
a = list(map(int,input().split()))
a.sort()
cnt=0
for i in range(n-1):
    if a[i]==a[i+1]:
        a[i]=0
        cnt+=1
if cnt%2==1:
    cnt+=1
print(n-cnt)
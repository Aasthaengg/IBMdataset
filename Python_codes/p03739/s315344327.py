n = int(input())
a = list(map(int, input().split()))

ans=float('inf')
s=0
cnt=0

for i in range(n):
    s+=a[i]
    if i%2==0:
        if s>=0:
            cnt+=1+s
            s=-1
    else:
        if s<=0:
            cnt+=1-s
            s=1
ans=min(ans,cnt)
s=0
cnt=0
for i in range(n):
    s+=a[i]
    if i%2==1:
        if s>=0:
            cnt+=1+s
            s=-1
    else:
        if s<=0:
            cnt+=1-s
            s=1
ans=min(ans,cnt)

print(ans)
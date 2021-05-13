n=int(input())
l=[0]*n
for i in range(n):
    a=int(input())
    l[a-1]=i
cnt=1;ans=0
for i in range(1,n):
    if l[i-1]>l[i]:
        if cnt>ans:ans=cnt
        cnt=1
        continue
    cnt+=1
print(n-ans if ans!=0 else 0)

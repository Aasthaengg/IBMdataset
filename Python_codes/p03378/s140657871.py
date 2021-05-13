n,m,x=map(int,input().split())
a=list(map(int,input().split()))
r=[0]*n
for i in range(m):
    r[a[i]-1]+=1
cnt_1=0
cnt_2=0
for i in range(x-1):
    cnt_1+=r[i]
for j in range(x,n):
    cnt_2+=r[j]
print(min(cnt_1,cnt_2))
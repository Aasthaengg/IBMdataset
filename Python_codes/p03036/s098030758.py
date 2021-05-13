r,D,initial=map(int,input().split())

ans=[0 for i  in range(10)]
ans[0]=initial*r-D


for i in range(1,10):
    ans[i]=ans[i-1]*r-D

for anss in ans:
    print(anss)


n,h,w=map(int,input().split())
cnt=0
for i in range(n):
    a,b=map(int,input().split())
    cnt+=min(a//h, b//w)
print(cnt)
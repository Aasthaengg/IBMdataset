n,h,w=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(n)]
# print(l)
cnt=0
for a,b in l:
    cnt+=min(a//h,b//w)
print(cnt)
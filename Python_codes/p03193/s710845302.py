n,h,w=map(int,input().split())
l=[list(map(int,input().split())) for i in range(n)]
cnt=0
for i in range(n):
    if l[i][0]>=h and l[i][1]>=w:
        cnt+=1
print(cnt)
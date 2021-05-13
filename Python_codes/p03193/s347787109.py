n,h,w=map(int,input().strip().split())
ab=[list(map(int,input().strip().split())) for i in range(n)]
cnt=0
for i in ab:
    if h<=i[0] and w<=i[1]:
        cnt+=1
print(cnt)
N,M=map(int,input().split())
s=[list(map(int,input().split())) for x in range(M)]

max_left=0
min_right=N

for i in range(M):
    if s[i][0]>max_left:
        max_left=s[i][0]
    if s[i][1]<min_right:
        min_right=s[i][1]
        
cnt=0
for j in range(max_left,min_right+1):
    cnt+=1
print(cnt)
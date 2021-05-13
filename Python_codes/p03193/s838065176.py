N,H,W=map(int,input().split())
A = []
B = []
for i in range(N):
    x1,y1=[int(i) for i in input().split()]
    A.append(x1)
    B.append(y1)

cnt=0

for i in range(N):
    if A[i]>=H and B[i]>=W:
        cnt+=1

print(cnt)
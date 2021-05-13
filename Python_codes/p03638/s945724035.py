H,W=map(int,input().split())
N=int(input())
A=list(map(int,input().split()))
ans0=[]
for i in range(N):
        ans0+=[i+1]*A[i]
ans0=ans0[::-1]

ans1=[[] for i in range(H)]
for i in range(H):
    for j in range(W):
        ans1[i].append(ans0.pop())

for i in range(H):
    if i%2==0:
        print(*ans1[i])
    else:
        print(*ans1[i][::-1])
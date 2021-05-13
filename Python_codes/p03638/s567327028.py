H,W = list(map(int,input().split()))
N = int(input())
A = list(map(int,input().split()))
cnt = 0
L = []
i = 1
while cnt<H*W:
    if A[i-1]>0:
        A[i-1]+=-1
        L.append(i)
        cnt+=1
    else:
        i+=1
for i in range(H):
    out = [0]*W
    if i%2==0:
        for j in range(W):
            out[j]=L[W*i+j]
    else:
        for j in range(W):
            out[W-1-j]=L[W*i+j]
    print(*out)
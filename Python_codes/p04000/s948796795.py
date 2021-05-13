import sys
input = sys.stdin.readline

H,W,N = map(int,input().split())
A = []
for i in range(N):
    a,b = map(int,input().split())
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if (1< a+i <H) and (1 < b+j < W):
                A.append([a+i,b+j])
A.sort()
ans = [0]*10
hoge = 0
for i in range(len(A)):
    if A[i] == A[i-1]:
        hoge += 1
    else:
        ans[hoge]+= 1
        hoge = 1
ans[hoge]+= 1


ans[0] = (W-2)*(H-2)-sum(ans[1:])

for i in ans:
    print(i)
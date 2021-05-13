N = int(input())
A = list(map(int,input().split()))
cmin = 104
for i in range(N):
    cnt = 1
    while A[i]%(2**cnt)==0:
        cnt += 1
    cmin = min(cmin,cnt-1)
print(cmin)
N = int(input())
H = list(map(int,input().split()))
cmax = 0
cnt = 0
for i in range(1,N):
    if H[i]<=H[i-1]:
        cnt += 1
    else:
        cmax = max(cmax,cnt)
        cnt = 0
cmax = max(cmax,cnt)
print(cmax)
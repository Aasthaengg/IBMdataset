N = int(input())
H = list(map(int,input().split()))
flag = 0
hmax = H[0]
for i in range(N):
    if H[i]<hmax-1:
        flag = 1
        break
    hmax = max(hmax,H[i])
if flag==1:
    print("No")
else:
    print("Yes")
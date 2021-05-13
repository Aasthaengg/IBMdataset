N = int(input())
H = list(map(int,input().split()))
flag = 0
hmax = H[0]
for i in range(1,N):
    h = H[i]
    if hmax-h>=2:
        flag = 1
        break
    hmax = max(hmax,h)
if flag==0:
    print("Yes")
else:
    print("No")
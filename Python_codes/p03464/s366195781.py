from math import ceil
k = int(input())
A = list(map(int,input().split()))[::-1]
if A[0]!=2:
    print(-1)
    exit()
flg = True
ans = [2,3]
for i in range(1, k):
    a = A[i]
    m = a*ceil(ans[0]/a)
    if m>ans[1]:
        flg = False
        break
    else:
        ans = [m,a*(ans[1]//a+1)-1]
if flg:
    print(*ans)
else:
    print(-1)
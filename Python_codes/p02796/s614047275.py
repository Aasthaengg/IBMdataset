N = int(input())
XL = [list(map(int,input().split())) for i in range(N)]

for i in range(N):
    XL[i].append(XL[i][0]+XL[i][1])
XL.sort(key=lambda x: x[2])

tmp = -1 * float('inf')
ans = 0
for X,L,right in XL:
    left = X-L
    if left >= tmp:
        tmp = right
        ans += 1
print(ans)
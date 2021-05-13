n   = int(input())
li  = list(map(int,input().split()))
ans  = [0]*n
ans2 = 0
ans3 = []
mtp  = 0

for i in range(n,0,-1):
    tmp = 0
    if n//i == 1:
        ans[i-1] = li[i-1]
    else:
        mtp = n//i
        for j in range(1,mtp):
            tmp += ans[i*(j+1)-1]
        tmp %= 2

        ans[i-1] = (tmp^li[i-1])

for i in range(n):
    if ans[i]==1:
        ans2 += 1
        ans3.append(i+1)

print(ans2)
print(*ans3)
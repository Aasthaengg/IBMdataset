N = int(input())
arr = list(map(int, input().split()))
ans = 0
flg = False
for i in range(1,N):
    if flg:
        flg = False
        continue
    if arr[i] == arr[i-1]:
        ans += 1
        flg = True
    else:
        flg = False
print(ans)
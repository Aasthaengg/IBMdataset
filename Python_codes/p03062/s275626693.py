N = int(input())
arr = list(map(int, input().split()))
cnt = 0
flg = False
for i in range(N):
    if arr[i] == 0:
        flg = True
    if arr[i] < 0:
        cnt += 1
    arr[i] = abs(arr[i])
if cnt % 2 == 0 or flg:
    print(sum(arr))
else:
    print(sum(arr) - min(arr)*2)
n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

def check(x):
    cnt, tmp = 0, 0
    for i in range(n):
        if x < arr[i]:
            return False
        elif tmp + arr[i] > x:
            tmp = arr[i]
            cnt += 1
        else:
            tmp += arr[i]
        if i == n - 1 and tmp > 0:
            cnt += 1
    return cnt <= k

l, r = 1, int(1e9 + 1)
while l < r:
    mid = (l + r) >> 1
    if check(mid):
        r = mid
    else:
        l = mid + 1
print(l)

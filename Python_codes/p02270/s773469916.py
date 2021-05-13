import math
n, k = map(int, input().split())
num = [int(input()) for i in range(n)]
#num.sort()
left = max(max(num), math.ceil(sum(num)/k))
right = sum(num)
while left < right:
    mid = (left + right) // 2
    track = 1
    cnt = 0
    flag = 0
    for i in num:
        cnt += i
        if cnt > mid:
            track+=1
            cnt = i
        if track > k:
            flag = 1
            break
        if flag:
            break
    if flag == 0:
        right = mid
    else:
        left = mid+1
print(left)

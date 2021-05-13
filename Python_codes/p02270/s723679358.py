def check(list, p, k):
    i = 0
    for j in range(k):
        sum = 0
        while sum+list[i] <= p:
            sum += list[i]
            i += 1
            if i == len(list):
                return i


    return i

nk = list(map(int, input().split()))
n = nk[0]
k = nk[1]

list = []
for i in range(n):
    list.append(int(input()))

max_num = 100000 * 10000

#二分探索で最大積載量の最小値を求める
left = 0
right = max_num
while left+1 < right:
    mid = int((left + right) /2)
    if check(list, mid, k) >= len(list):
        right = mid
    else:
        left = mid

print(right)


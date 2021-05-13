def unit_check(n, k, w_list, P):
    i = 0
    for j in range(k):
        weight = 0
        while weight + w_list[i] <= P:
            weight += w_list[i]
            i += 1
            if i == n:
                return 1
    return 0

n, k = map(int,input().split())
w_list = [0] * n
for i in range(n):
    w_list[i] = int(input())

left = 0
right = 100000*10000
while left+1 < right:
    mid = (left+ right)//2
    check = unit_check(n, k, w_list, mid)
    if check == 1:
        right = mid
    else:
        left = mid
print(right)

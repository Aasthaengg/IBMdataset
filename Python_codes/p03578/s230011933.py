n = int(input()) # 入力が1つ
# map(int, input().split()) # 入力が複数
d = [int(i) for i in input().split()] # 配列で数字

m = int(input()) # 入力が1つ
# map(int, input().split()) # 入力が複数
t = [int(i) for i in input().split()]

def bs(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1

if n < m:
    print('NO')
else:
    d.sort()
    t.sort()
    i = j = 0
    while i < n and j < m:
        if d[i] == t[j]:
            i += 1
            j += 1
        else:
            i += 1
    if j == m:
        print('YES')
    else:
        print('NO')
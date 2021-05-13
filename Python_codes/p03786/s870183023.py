n = int(input())
arr = sorted([int(a) for a in input().split()])

res = 0
size = 0
for i in range(n-1):
    size += arr[i]
    if arr[i+1] > size * 2:
        res = 0
    else:
        res += 1
res += 1

print(res)

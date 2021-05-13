n = int(input())
aa = list(map(int, input().split()))

border = 3200 // 400
arr = [0] * 8
over = 0
for a in aa:
    x = a // 400

    if x >= border:
        over += 1
        continue

    arr[x] = 1

s = sum(arr)

print(max(1, s), s + over)

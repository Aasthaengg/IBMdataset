a, b, k = map(int, input().split())
cnt = 0
num = min(a, b) + 1
while cnt < k:
    num -= 1
    if a % num == 0 and b % num == 0:
        cnt += 1
print(num)

a, b, k = map(int, input().split())

num = min(a, b)

cnt = 0

while cnt < k:
    if a%num == 0 and b%num == 0:
        cnt += 1
        num -= 1
    else:
        num -= 1
print(num + 1)
n, k = map(int, input().split())
apple = []
orange = []
for _ in range(n):
    apple.append(int(input()))
a = sorted(apple)
for i in range(n - k):
    b = - a[i] + a[i + k -1]
    c = a[-i-1] - a[-(i + k)]
    if b != 0 or c != 0:
        orange.append(min(b, c))
    else:
        orange.append(0)
        break
print(min(orange))
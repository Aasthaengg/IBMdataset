a, b, c = sorted(map(int, input().split()))
x = b - a
cnt = c - b + x // 2
print((cnt + 2, cnt)[x % 2 == 0])
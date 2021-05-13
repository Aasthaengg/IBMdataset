N = int(input())
a = list(map(int, input().split()))

c = [0] * 8
r = 0

for i in a:
    col = i // 400
    if col <= 7:
        c[col] = 1
    else:
        r += 1

c = sum(c)

print(max(1, c), r+c)
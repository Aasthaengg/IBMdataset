h = int(input())
w = int(input())
n = int(input())
ans = 0

while True:
    if h >= w:
        n = n - h
    else:
        n = n - w

    ans = ans + 1

    if n <= 0:
        break

print(ans)
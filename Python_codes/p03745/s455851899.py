n = int(input())
a = list(map(int, input().split()))

up = False
down = False
ans = 1

for i in range(1, n):
    if up:
        if a[i] < a[i-1]:
            ans += 1
            up = False
    elif down:
        if a[i] > a[i-1]:
            ans += 1
            down = False
    else:
        if a[i] > a[i-1]:
            up = True
        elif a[i] < a[i-1]:
            down = True

print(ans)
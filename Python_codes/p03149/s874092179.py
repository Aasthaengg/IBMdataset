n = list(map(int, input().split()))
f = 0
for i in n:
    if i == 1:
        f += 1
    elif i == 7:
        f += 10
    elif i == 9:
        f += 100
    elif i == 4:
        f += 1000
print("YES" if f == 1111 else "NO")
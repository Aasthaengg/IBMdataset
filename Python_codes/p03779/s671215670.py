X = int(input())
ans = -1
c = 0
for i in range(1, 10**6):
    c += i
    if 0 <= c - X <= i:
        ans = i
        break
print(ans)
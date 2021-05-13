x = int(input())

ans = 0
total = 0
for i in range(1, 10**9):
    total += i
    if total >= x:
        ans = i
        break

print(ans)
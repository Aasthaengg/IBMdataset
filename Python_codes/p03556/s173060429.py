N = int(input())

ans = 0

for i in range(10**5):
    if i ** 2 <= N:
        ans = i ** 2
        continue
    break

print(ans)
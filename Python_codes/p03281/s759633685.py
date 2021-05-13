n = int(input())

divs = [0] * (n + 1)
for i in range(1, (n + 1)):
    for j in range(i, (n + 1), i):
        divs[j] += 1

ans = 0

for idx, div in enumerate(divs):
    if div == 8 and idx % 2 == 1:
        ans += 1

print(ans)

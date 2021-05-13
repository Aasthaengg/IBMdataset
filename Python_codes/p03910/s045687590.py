n = int(input())
if n == 1 or n == 2:
    print(n)
    exit()

now = 0
ans = []
for i in range(1, n):
    now += i
    ans.append(i)
    if now >= n:
        break

amari = now - n

for i in ans:
    if i == amari:
        continue
    else:
        print(i)

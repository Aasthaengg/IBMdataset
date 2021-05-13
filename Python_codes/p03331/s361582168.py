n = int(input())

if n == 10 or n == 100 or n == 1000 or n == 10000 or n == 100000:
    ans = 10
else:
    n = str(n)
    ans = 0
    for l in n:
        ans += int(l)

print(ans)
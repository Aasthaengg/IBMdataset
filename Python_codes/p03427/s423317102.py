n = list(input())
ans = 0

a = (len(n) - 1) * 9 + int(n[0]) - 1

if a < sum(map(int, n)):
    ans = sum(map(int, n))
else:
    ans = a

print(ans)
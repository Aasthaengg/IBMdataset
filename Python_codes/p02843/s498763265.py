X=int(input())

p = X % 100
q = p // 5
r = p % 5
ans = q
if r > 0:
    ans += 1
ans = ans * 100 + p
if X >= ans:
    print(1)
else:
    print(0)
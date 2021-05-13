s = int(input())
a = [True] * 1000001
ans = 1
while a[s]:
    a[s] = False
    ans += 1
    if s % 2 == 0:
        s //= 2
    else:
        s = s * 3 + 1
print(ans)

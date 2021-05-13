n = input()
ans = 100000
for i in xrange(n):
    ans *= 1.05
    if ans % 1000 > 0:
        ans += 1000 - (ans % 1000)
print int(ans)
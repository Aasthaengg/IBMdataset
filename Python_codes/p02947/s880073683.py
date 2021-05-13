n = int(input())
pr = {}
ans = 0
for i in range(n):
    s = input()
    s = ''.join(sorted(s))
    if s in pr:
        pr[s] += 1
        ans += pr[s]
    else:
        pr[s] = 0
print(ans)

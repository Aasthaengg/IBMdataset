n = int(input())
ans = 0
ls = {}
for _ in range(n):
    s = ''.join(sorted(input()))
    if s in ls:
        ans += ls[s]
        ls[s] += 1
    else:
        ls[s] = 1
print(ans)
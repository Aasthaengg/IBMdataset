N = input()
ans = sum(int(c) for c in N)

for i in range(1,len(N)):
    t = sum(int(c) for c in N[:i]) - 1 + 9 * (len(N) - i)
    ans = max(ans, t)
print(ans)
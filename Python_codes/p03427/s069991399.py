N = input()
l = len(N)
ans = sum([int(n) for n in N])
ans = max(ans, (int(N[0])-1)+(l-1)*9)
print(ans)

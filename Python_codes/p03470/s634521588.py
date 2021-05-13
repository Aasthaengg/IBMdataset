N = int(input())
d = list(map(int, [input() for i in range(N)]))

ans = len(set(d))

print(ans)
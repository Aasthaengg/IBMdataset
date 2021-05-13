N, L = map(int, input().split())
v = [L+i for i in range(N)]
ans = sum(v) - min(v, key=abs)
print(ans)

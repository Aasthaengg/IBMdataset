N = int(input())
p = list(int(input()) for i in range(N))

ans = sum(p) - max(p) // 2
print(ans)
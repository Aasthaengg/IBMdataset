n = int(input())
p = [int(input()) for i in range(n)]
p1 = sorted(p)
a = p1.pop(-1)
a1 = a // 2
ans = sum(p1)
ans += a1
print(ans)
n = int(input())
p = [int(input()) for _ in range(n)]
s = sorted(p, reverse=True)
print((s[0]//2)+sum(s[1:]))

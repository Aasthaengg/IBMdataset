q, h, s, d = map(int, input().split())
n = int(input())
s = min(4*q, 2*h, s)
ans = n//2*min(2*s, d)
ans += s*(n%2)
print(ans)
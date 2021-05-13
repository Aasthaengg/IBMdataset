n = int(input())
s = list(map(int, input().split()))
s.sort()
x = n // 2
print(s[x] - s[x - 1] if s[x] != s[x - 1] else 0)
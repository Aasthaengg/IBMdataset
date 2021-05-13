n, l = map(int, input().split())
s = [0] * n
for i in range(n):
    s[i] = i + l
s.sort(key=abs)
print(sum(s[1:]))

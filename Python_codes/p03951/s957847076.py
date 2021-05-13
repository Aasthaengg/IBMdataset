n = int(input())
s = input()
t = input()
ans = n * 2
for i in range(n):
    if s == t:
        ans -= n - i
        break
    s = s[1:]
    t = t[:-1]
print(ans)

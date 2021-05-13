n = int(input())
s = input()
t = input()
ans = n
for i in range(n):
    f = True
    for j in range(n - i):
        f &= s[j + i] == t[j]
    if f:
        ans = i
        break
print(n+ans)

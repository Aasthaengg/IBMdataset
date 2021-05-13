n = int(input())
s = []
t = []
for _ in range(n):
    si, ti = input().split()
    s.append(si)
    t.append(int(ti))
x = input()
ans = sum(t)
for i in range(n):
    ans -= t[i]
    if s[i] == x:
        break
print(ans)

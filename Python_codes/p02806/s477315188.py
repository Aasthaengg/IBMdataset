N = int(input())

s = []
t = []
for i in range(N):
    a,b = input().split()
    s.append(a)
    t.append(int(b))
x = input()

f = False
ans = 0
for i in range(N):
    if f:
        ans += t[i]
    else:
        if x == s[i]:
            f = True

print(ans)

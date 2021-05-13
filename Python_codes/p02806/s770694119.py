n = int(input())
s = [0] * n
t = [0] * n
for i in range(n):
    s[i], t[i] = map(str, input().split())
    t[i] = int(t[i])
x = input()
ans = 0
flag = False
for i, v in zip(s, t):
    if i == x:
        flag = True
        continue
    if flag:
        ans += v
print(ans)
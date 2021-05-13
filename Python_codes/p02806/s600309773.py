n = int(input())
sl = []
tl = []
for _ in range(n):
    s, t = input().split()
    sl.append(s)
    tl.append(int(t))
x = input()

ans = 0
flag = False
for i in range(n):
    if flag:
        ans += tl[i]
    if sl[i] == x:
        flag = True
print(ans)

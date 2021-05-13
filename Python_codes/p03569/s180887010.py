#末端の処理を変更
s_ = "x"+input()+"x"
s = []
c = []
cnt = 0
"""
if s_[0]!="x":
    c.append(0)
"""
for i in range(len(s_)):
    if s_[i]!="x":
        c.append(cnt)
        cnt = 0
        s.append(s_[i])
    else:
        cnt += 1
c.append(cnt)

l = len(s)
for i in range(l//2):
    if s[i]!=s[l-i-1]:
        print(-1)
        exit()
ans = 0
l2 = len(c)
for i in range(l2):
    ans += abs(c[i]-c[l2-i-1])

print(ans//2)

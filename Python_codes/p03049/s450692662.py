n = int(input())
s = []
for _ in range(n):
    s.append(input())
a = 0
b = 0
ans = 0
same = 0
for i in s:
    flg = False
    if i[0]=='B':
        flg = True
        b += 1
    if i[-1]=='A':
        a += 1
        if flg:
            same += 1
    for j in range(len(i)-1):
        if i[j:j+2]=='AB':
            ans += 1
ans += min(a, b)
if a == b == same > 0:
    ans -= 1
print(ans)
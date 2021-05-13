N = int(input())
s = []
for _ in range(N):
    s.append(input())

in_str = 0
BX = 0
XA = 0
BA = 0
for str in s:
    in_str += str.count('AB')
    if str[0] == 'B' and str[-1] != 'A':
        BX += 1
    elif str[0] != 'B' and str[-1] == 'A':
        XA += 1
    elif str[0] == 'B' and str[-1] == 'A':
        BA += 1

ans = in_str
if min(XA, BX) >= 1:
    ans += BA + min(XA, BX)
elif max(BX, XA) == 0:
    ans += max(0, BA - 1)
else:
    ans += 1 + BA - 1
print(ans)
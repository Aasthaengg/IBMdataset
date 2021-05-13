n = int(input().strip())
s1 = input().strip()
s2 = input().strip()
mod = 1000000007
vert = False
hor1 = False
hor2 = False

if s1[0] == s2[0]:
    ans = 3
    vert = True
else:
    ans = 6
    hor1 = True
for i in range(1, n):
    if s1[i] == s2[i]:
        if vert:
            ans = (ans * 2) % mod
        vert = True
        hor1 = False
        hor2 = False
    else:
        if vert:
            ans = (ans * 2) % mod
            vert = False
            hor1 = True
            hor2 = False
        elif hor1:
            vert = False
            hor1 = False
            hor2 = True
        elif hor2:
            ans = (ans * 3) % mod
            vert = False
            hor1 = True
            hor2 = False
print(ans)

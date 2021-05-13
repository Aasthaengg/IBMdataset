N = r = int(input())
l = 0
print(0)
S = input()
if S == "Vacant":
    exit()
while l < r - 1:
    m = (l + r) // 2
    print(m)
    s = input()
    if s == "Vacant":
        exit()
    if l & 1 == m & 1 and S == s or l & 1 != m & 1 and S != s:
        l = m
        S = s
    else:
        r = m
print(l)
input()
exit()
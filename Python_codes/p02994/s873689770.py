n,l = map(int,input().split())
azi = list()
for i in range(n):
    azi.append(l+i)
kei = sum(azi)
s = list()
for i in range(n):
    s.append(kei-azi[i])

tmp = float('inf')
ans = 0
for i in range(n):
    if tmp >= abs(kei-s[i]):
        ans = s[i]
        tmp = abs(kei-s[i])
print(ans)
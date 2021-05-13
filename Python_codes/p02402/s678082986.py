count = int(raw_input())
lis = map(int, raw_input().split())
mi = lis[0]
ma = lis[0]
su = 0
for i in lis:
    if i < mi:
        mi = i
    if i > ma:
        ma = i
    su += i

print '%d %d %d'%(mi, ma, su)
from itertools import permutations
n = int(input())
s = [input() for i in range(n)]
lsa=list() #mn,end
lsd=list()
for i in range(n):
    now = 0
    mn = 0
    for c in s[i]:
        if c == '(':
            now += 1
        else:
            now -= 1
            mn = min(mn,now)
    if now >= 0:
        lsa.append([mn,now])
    else:
        lsd.append([mn-now,-now])

lsa.sort(reverse=True)
tmn = 0
tend = 0
flag=True
# ascent
for mn,end in lsa:
    tmn = mn + tend
    tend += end
    if tmn < 0 or tend < 0:
        flag = False
        break
tenda = tend

# descent
lsd.sort(reverse=True)
tmn = 0
tend = 0

for mn,end in lsd:
    tmn = mn + tend
    tend += end
    if tmn < 0 or tend < 0:
        flag=False
        break

if flag and tend == tenda:
    print("Yes")
else:
    print("No")




n,k = map(int,input().split())
s = input()
cou = 0
p = 1
nagasa = []
for i in range(n):
    if int(s[i]) == p:
        cou += 1
    elif int(s[i]) != p:
        if p == 1:
            p = 0
        elif p == 0:
            p = 1
        nagasa.append(cou)
        cou = 1
nagasa.append(cou)
if len(nagasa) % 2 == 0:
    nagasa.append(0)
h = len(nagasa)

if h // 2 <= k:
    print(n)
    exit()
lef = 0
rig = 2*k+1
now = sum(nagasa[lef:rig])
ans = now
while True:
    if rig == h:
        break
    now = now - nagasa[lef] - nagasa[lef+1] + nagasa[rig] + nagasa[rig+1]
    ans = max(ans,now)
    lef += 2
    rig += 2
print(ans)

import itertools

n = int(input())

name = {"M":[],"A":[],"R":[],"C":[],"H":[]}
for i in range(n):
    s = input()
    if s[0] not in name:
        continue
    else:
        name[s[0]].append(s)

ans = 0
for p,q,r in itertools.combinations(name.keys(), 3):
    ans += len(name[p])*len(name[q])*len(name[r])
    
print(ans)
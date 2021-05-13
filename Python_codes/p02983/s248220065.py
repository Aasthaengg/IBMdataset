l, r = map( int, input().split())

amr = []
for x in range(l,r+1):
    if len(amr) >= 2019:
        break
    amr.append(x%2019)
# print(amr)
amr = list(set(amr))
ij_mod = []
for i in range(len(amr)-1):
    for j in range(i+1,len(amr)):
        ij_mod.append((amr[i]*amr[j])%2019)
print(min(ij_mod))



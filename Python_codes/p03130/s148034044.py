#どの 2 つの街の間も、道を何本か通ることで行き来することができる
cnts=[0]*4
for i in range(3):
    ai,bi=map(int, input().split())
    ai-=1;bi-=1
    cnts[ai]+=1;cnts[bi]+=1
for i in range(4):
    if cnts[i]>2:
        print("NO")
        exit()
print("YES")

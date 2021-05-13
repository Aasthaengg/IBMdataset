M = "#."*151
ans = []
add = ans.append
for line in open(0).readlines():
    H, W = map(int, line.split())
    if not H:
        break
    for i in range(H):
        j = i%2
        add(M[j:W+j])
        add("\n")
    add("\n")
open(1, 'w').writelines(ans)

from itertools import product 

n = int(input())
XY = [[] for _ in range(n)]
for i in range(n):
    a = int(input())
    for _ in range(a):
        x, y = map(int, input().split())          
        XY[i].append((x-1,y))
ans = 0
bits = list(product([0,1],repeat=n))
for bit in bits:
    honest_tes = []
    honest_idx = []
    honest_list = [0 for _ in range(n)]
    flag = True
    for who, h in enumerate(bit):
        if h == 1:
            honest_tes.append(XY[who])
            honest_idx.append(who)
            honest_list[who] = 1
    for idx in honest_idx:
        for x, y in XY[idx]:
            if honest_list[x] != y:
                flag = False
                break
    if flag:
        ans = max(ans, len(honest_idx))
print(ans)
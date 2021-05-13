N, M = map(int, input().split())
lst = [input().split() for _ in range(M)]
pe = [0] * N #結果的なWA数
wa = [0] * N #現在のWA数（ACしたら-1）

for l in lst:
    if l[1] == "WA" and wa[int(l[0])-1] != -1:
        #未ACでWA
        wa[int(l[0])-1] += 1
    if l[1] == "AC" and wa[int(l[0])-1] != -1:
        #はじめてAC
        pe[int(l[0])-1] = wa[int(l[0])-1]
        wa[int(l[0])-1] = -1

ans = []
ans.append(str(wa.count(-1)))
ans.append(str(sum(pe)))
print(" ".join(ans))
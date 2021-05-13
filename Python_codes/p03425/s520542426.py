import collections

N = int(input())
S = [str(input())[0] for _ in range(N)]
ref_lst = [["M",0],["A",0],["R",0],["C",0],["H",0]]

for i in range(5):
    ref_lst[i][1] = S.count(ref_lst[i][0])

ans = 0
for j in range(5):
    for k in range(j+1,5):
        for l in range(k+1,5):
            ans += ref_lst[j][1]*ref_lst[k][1]*ref_lst[l][1]

print(ans)
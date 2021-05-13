from itertools import product 
n,a,b,c = map(int,input().split())
l = [int(input()) for _ in range(n)]
tar = [a,b,c]
ans = float("inf")
for p in product(range(4),repeat=n):
    mp = 0
    length = [0]*3
    for i,j in enumerate(p):
        if j == 3: continue
        if length[j] > 0: mp += 10
        length[j] += l[i]
    for j in range(3):
        if length[j] == 0: break
        mp += abs(length[j]-tar[j])
    else:
        ans = min(ans, mp)
print(ans)
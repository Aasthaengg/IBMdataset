from itertools import combinations_with_replacement

n,m,q = map(int,input().split())
L = [list(map(int,input().split())) for i in range(q)]

#重複組み合わせ
ans = 0
for i in combinations_with_replacement(range(m),n):
    t = 0
    for a,b,c,d in L:
        if i[b-1] - i[a-1] == c:
            t += d
    ans = max(ans,t)

print(ans)
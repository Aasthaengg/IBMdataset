#21 D - Banned K AC TLE(hint)
import collections
N = int(input())
A = list(map(int,input().split()))

cnt = collections.Counter(A)
#先に組み合わせの個数を計算しておく
combinations = {}
for j in cnt.keys():
    if cnt[j] >= 2:
        comb = (cnt[j]*(cnt[j]-1))//2
        combinations[j] = comb      

#あるボールを選ばないとき、組み合わせの総数は
#(全組み合わせ数) - (選ばないボールと同じボールの数 - 1)
tot = sum(combinations.values())
ans = []
for i in A:
    a = tot - (cnt[i] - 1)
    ans.append(a)
    
for k in ans:
    print(k)
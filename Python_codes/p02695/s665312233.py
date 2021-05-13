from itertools import combinations_with_replacement

n,m,q = map(int,input().split())
s_list = [list(map(int,input().split())) for _ in range(q)]

ans = 0
for c in combinations_with_replacement(range(1,m+1),n):
    v = 0
    for s in s_list:
        if c[s[1]-1] - c[s[0]-1] == s[2]:
            v+=s[3]
    
    ans = max(ans,v)
print(ans)
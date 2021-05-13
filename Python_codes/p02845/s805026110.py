input()
v = [0,0,0]
ans = 1
MOD = 1000000007
for a in map(int,input().split()):
    c = v.count(a)
    ans *= c
    ans %= MOD
    if ans == 0:
        break
    v[v.index(a)] += 1
print(ans)

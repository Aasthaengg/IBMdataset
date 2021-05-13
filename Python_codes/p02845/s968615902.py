n = int(input())
A = list(map(int, input().split()))
ans = 1
MOD = 1000000007
c = [0, 0, 0]
for a in A:
    cnt = c.count(a)
    if cnt == 0:
        print(0)
        exit()
    ans *= cnt
    ans %= MOD
    c[c.index(a)] += 1
print(ans)
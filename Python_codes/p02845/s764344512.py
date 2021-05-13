N = int(input())
A = tuple(map(int, input().split()))
MOD = 1000000007

ct = [0, 0, 0]
ans = 1
for a in A:
    cta = ct.count(a)
    if cta:
        ct[ct.index(a)] += 1
        ans = (ans * cta) % MOD
    else:
        print(0)
        exit()
print(ans)

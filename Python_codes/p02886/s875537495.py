import itertools
N = int(input())
Nlist = list(map(int, input().split()))
c = list(itertools.combinations(Nlist, 2))
ans = 0
for i in c:
    ans += i[0]*i[1]
print(ans)

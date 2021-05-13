import itertools as it 
N = int(input())
d = list(map(int,input().split()))

l = list(it.combinations(d,2))

ans = 0
for i in range(len(l)):
    ans += l[i][0] * l[i][1]

print(ans)
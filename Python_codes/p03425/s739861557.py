import itertools
n = int(input())
s = [input()[0] for i in range(n)]

c = [s.count(i) for i in 'MARCH']
ans = sum(c[i]*c[j]*c[k] for i,j,k in itertools.combinations(range(5), 3))
print(ans)
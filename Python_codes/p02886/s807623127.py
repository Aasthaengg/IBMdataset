import itertools
N = int(input())
d = list(map(int, input().split()))

p = list(itertools.permutations(d,2))


n = 0

for i in range(len(p)):
    n = n + (p[i][0] * p[i][1])
    
A = int(n/2)
print(A)

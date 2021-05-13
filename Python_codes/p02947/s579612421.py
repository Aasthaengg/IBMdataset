import collections
N = int(input())
lsS = []
for i in range(N):
    lsS.append(''.join(sorted(input())))

counter = collections.Counter(lsS)
n=0
for i in counter.values():
    n+= (i*(i-1))//2
print(n)
import itertools
def distance(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
n = int(input())
a = [tuple(map(int,input().split())) for _ in range(n)]
l = []
for m in list(itertools.permutations(a)):
    d = 0
    for i in range(n-1):
        d += distance(m[i],m[i+1])
    l.append(d)
print(sum(l)/len(l))
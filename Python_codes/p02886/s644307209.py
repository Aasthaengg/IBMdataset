import itertools
n = int(input())
d = list(map(int,input().split()))
a = (list(itertools.permutations(d,2)))
b = []
for i in range(len(a)):
    b.append(a[i][0]*a[i][1])
print(sum(b)//2)
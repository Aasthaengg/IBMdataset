import sys
input = sys.stdin.readline
import itertools

N=int(input())
x = []
y = []
for _ in range(N):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)
ls = []
for arr in itertools.permutations(list(range(N))):
    l = 0
    for ii in range(len(arr)-1):
        i = arr[ii]
        j = arr[ii+1]
        d = ((x[i]-x[j])**2 + (y[i]-y[j])**2)**0.5
        l += d
    ls.append(l)

print(sum(ls)/len(ls))




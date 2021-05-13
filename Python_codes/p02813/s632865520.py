import sys
import itertools
input = sys.stdin.readline

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

l = list(range(1, n+1))

i = 0
s = 0
t = 0
#print(p)
for v in itertools.permutations(l):
    #print(v)
    if v == p:
        s = i
    if v == q:
        t = i
    
    i += 1

print(abs(t - s))

import sys
from itertools import permutations
input = sys.stdin.readline

n=int(input())
p=tuple(map(int,input().split()))
q=tuple(map(int,input().split()))

L=list(permutations(list(range(1,n+1))))
print(abs(L.index(p)-L.index(q)))

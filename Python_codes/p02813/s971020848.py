n=int(input())
a=tuple(map(int, input().split()))
b=tuple(map(int, input().split()))
cnta=0
cntb=0
li=[i for i in range(1,n+1)]
import itertools
k=0
for i in itertools.permutations(li):
    if tuple(i)==a:
        cnta=k
    if tuple(i)==b:
        cntb=k
    k+=1
print(abs(cnta-cntb))
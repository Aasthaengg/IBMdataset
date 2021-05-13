from itertools import combinations, product
*_,k=map(int,input().split())
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
c=[int(i) for i in input().split()]
ab=[]
for i,j in product(a,b):
    ab.append(i+j)
ab.sort(reverse=True)
ab = ab[:k]
abc = []
for i,j in product(ab,c):
    abc.append(i+j)

abc.sort(reverse=True)
print(*abc[:k],sep="\n")
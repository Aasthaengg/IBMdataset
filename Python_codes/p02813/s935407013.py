from itertools import permutations
n=int(input())
p=tuple(map(int,input().split()))
q=tuple(map(int,input().split()))

array=[]

for i in range(1,n+1):
	array.append(i)

z=list(permutations(array,n))

a=z.index(p)
b=z.index(q)

print(abs((a+1)-(b+1)))
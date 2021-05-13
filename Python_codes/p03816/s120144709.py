import collections
N=int(input())
A=list(map(int,input().split()))

c=collections.Counter(A)
values=list(c.values())	#aのCollectionのvalue値のリスト(n_1こ、n_2こ…)
for i in range(len(values)):
    values[i]=(values[i]-1)%2
print(len(values)-sum(values)%2)
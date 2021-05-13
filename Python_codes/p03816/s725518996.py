import collections
N=int(input())
A=list(map(int,input().split()))
"""
c=collections.Counter(A)
values=list(c.values())	#aのCollectionのvalue値のリスト(n_1こ、n_2こ…)
for i in range(len(values)):
    values[i]=(values[i]-1)%2
print(len(values)-sum(values)%2)
"""
#""Nが奇数なので""
#len(set(A))%2==0なら取り除きたい最小限のカードの枚数は偶数、それらそのまま除くことが可能である
#len(set(A))%2==1なら取り除きたい最小限のカードの枚数は奇数、そのままは除けず、1枚犠牲になる
print(len(set(A))-(len(set(A))+1)%2)
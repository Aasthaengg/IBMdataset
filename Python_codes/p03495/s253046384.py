from collections import Counter
n,k=map(int,input().split())
a=list(sorted(Counter(list(map(int,input().split()))).values()))
print(sum(a[:len(a)-k]))
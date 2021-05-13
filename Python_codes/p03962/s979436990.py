from collections import Counter

abc=list(map(int,input().split()))
c=Counter(abc)
print(len(c))
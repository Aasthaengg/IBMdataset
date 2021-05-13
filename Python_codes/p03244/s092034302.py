from collections import Counter

n=int(input())
v=list(map(int,input().split()))

e=Counter(v[::2]).most_common() + [(0,0)]
o=Counter(v[1::2]).most_common() + [(0,0)]


if e[0][0]!=o[0][0]:
    print(n-e[0][1]-o[0][1])
else:
    print(min(n-e[0][1]-o[1][1],n-e[1][1]-o[0][1]))    

N=int(input())
S=[]
for _ in range(N):
    _=input()
    S.append(_)
import collections
a=collections.Counter(S)
b=max(a.values())
new_a=[k for k, v in a.items() if v==b]
new_a.sort()
for i in range(len(new_a)):
    print(new_a[i])



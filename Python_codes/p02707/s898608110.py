import collections
n = int(input())
A = list(map(int,input().split()))
Ac = collections.Counter(A)
for i in range(1,n+1):
    if i in Ac.keys():
        print(Ac[i])
    else:
        print(0)

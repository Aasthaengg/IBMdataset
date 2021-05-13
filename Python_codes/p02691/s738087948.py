from collections import defaultdict
n=int(input())
a=list(map(int,input().split()))
d=defaultdict(int)
for i in range(n):
    d[i+1-a[i]]+=1
print(sum(d[i+1+a[i]] for i in range(n)))
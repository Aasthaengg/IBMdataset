import collections

n = int(input())
s=[]
for i in range(n):
    s.append(input())

c = collections.Counter(s) 

print(len(c))
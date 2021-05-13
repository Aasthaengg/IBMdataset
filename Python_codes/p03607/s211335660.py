import collections
N= int(input())
A = sorted(list(int(input()) for i in range(N)))
c = collections.Counter(A)
count = 0

for v in c.values():
    if v%2 !=0:
        count +=1 

print(count)
from collections import Counter
n=int(input())
c=Counter([int(input())for i in range(n)])
a=0
for i in c.values():a+=1if i%2else 0
print(a)
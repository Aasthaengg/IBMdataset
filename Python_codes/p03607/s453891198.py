from collections import Counter
n=int(input())
a=[int(input()) for _ in range(n)]
c=Counter(a)
ret=0
for list in c.items():
    if list[1]%2==1:
        ret+=1
print(ret)
import collections

n=int(input())
lst=[]
ans=0

for i in range(n):
    s=input()
    lst.append(''.join(sorted(s)))

c=collections.Counter(lst)

for i in set(lst):
    x=c[i]

    ans+=x*(x-1)//2


print(ans)
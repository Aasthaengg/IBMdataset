import collections
n=int(input())
lst=[int(i) for i in input().split()]
c = collections.Counter(lst)
change=0
for i,count in c.items():
    if(count>1):
        change+=count-1
if (change%2!=0):
    change+=1
ans=n-change
print(ans)
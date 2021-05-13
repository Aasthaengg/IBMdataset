from math import ceil
n=int(input())
p=input().split()
ans=0
l=['0']*len(p)
for i in range(len(p)):
    if i+1==int(p[i]):
        l[i]='1'
s=''.join(l)

l=s.split('0')

for j in l:
    ans+=ceil(len(j)/2)
print(ans)

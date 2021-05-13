n=int(input())
s=list(input())
r=s.count('R')
b=n-r
if b<r:
    print('Yes')
else:
    print('No')
N=int(input())
c=input()
count=0

if 'WR' in c:
    x=c.count('R')
    y=c.count('R',0,x)
    count=x-y
print(count)
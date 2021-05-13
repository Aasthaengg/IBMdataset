a,b,c=map(int,input().split())
d=a+b
total=0
if c>d:
    total=2*d+1
elif c==d:
    total=2*d
else:
    total=c+d
print(total-a)
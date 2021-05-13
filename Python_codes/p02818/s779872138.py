a,b,k=map(int, input().split())

if a>=k:
    x,y=a-k,b
elif a+b >= k:
    x,y=0,b-(k-a)
else:
    x,y=0,0
print('{} {}'.format(x,y))
a,b,c=map(int,input().split())
a,b,c=min(a,b,c),a+b+c-max(a,b,c)-min(a,b,c),max(a,b,c)
print(a*b*(c%2))
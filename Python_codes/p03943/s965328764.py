a,b,c=map(int,input().split())
t=a+b+c
k=0 if a+b==c or a+c==b or b+c==a else 1
print(['Yes','No'][k])

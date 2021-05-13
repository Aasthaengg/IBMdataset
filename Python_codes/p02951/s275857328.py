a,b,c=map(int,input().split())
if c>=a-b:
    c=c-a+b
else: c=0
print(c)

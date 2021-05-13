s={}
s['a']=list(input())
s['b']=list(input())
s['c']=list(input())
x='a'
while(s[x]):
    x=s[x].pop(0)
print(x.upper())

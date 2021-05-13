n=int(input())
a={}
for i in range(n):
    key=input()
    if key in a:
        a[key]+=1
    else:
        a[key]=1
b=max(list(a.values()))
c=[]
for k,v in a.items():
    if v==b:
        c.append(k)
c=sorted(c)
for i in range(len(c)):
    print(c[i])
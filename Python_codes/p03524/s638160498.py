def mycounter(d,i):
    if i in d:
        d[i]+=1
    else:
        d[i]=1
    return d
s=input()
d=dict()
for i in s:
    d=mycounter(d,i)
l=-(-len(s)//3)
for i in d.values():
    if l<i:
        print('NO')
        exit()
print('YES')
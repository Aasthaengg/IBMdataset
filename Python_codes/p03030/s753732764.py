n = int(input())
sp = {i+1:input().split() for i in range(n)}

d = []
for i,s in sp.items():
    d.append((i,s[0],int(s[1])))
    
d = sorted(d,key=lambda x:x[2],reverse=True)
d = sorted(d,key=lambda x:x[1])
    
    
for i in d:
    print(i[0])

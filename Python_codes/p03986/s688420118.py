x=input()
l=len(x)
ans=0
q=[]
for i in range(l):
    if x[i]=='S':
        q.append(x[i])
    else:
        if not q or q[-1]=='T':
            q.append(x[i])
        else:
            q.pop()
            ans+=1
print(l-ans*2)

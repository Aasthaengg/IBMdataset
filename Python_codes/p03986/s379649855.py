X=input()
q = []
for x in X:
    if x=='S':
        q.append(x)
    else:
        if len(q)==0 or q[-1]=='T':
            q.append(x)
        else:
            q.pop()
print(len(q))

w=list(input())
W=list(set(w))
a=[]
for i in range(len(W)):
    a.append(w.count(W[i]))
b=[]
for i in range(len(a)):
    if a[i]%2==0:
        b.append('yes')
    else:
        b.append('no')
if 'no' in b:
    print('No')
else:
    print('Yes')
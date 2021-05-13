q=(input())
A=(list(q))
S=map((lambda x: int(x)),A)
W=sum(S)
if W%9==0:
    print('Yes')
else:
    print('No')
s=list(input())
t=list(input())
s=sorted(s)
t=sorted(t,reverse=True)
s=''.join(s)
t=''.join(t)
if t>s:
    print('Yes')
else:
    print('No')


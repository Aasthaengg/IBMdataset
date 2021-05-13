s=input()
t=input()

s=''.join(sorted(s))
t=''.join(sorted(t,reverse=True))

if t>s:
    print('Yes')
else:
    print('No')
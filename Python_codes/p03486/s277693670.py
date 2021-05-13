s,t=list(input()),list(input())
if s==t: print('No');exit()
s.sort();t.sort(reverse=True)
l=[''.join(s),''.join(t)]
r=sorted(l)
print('Yes' if l==r else 'No')
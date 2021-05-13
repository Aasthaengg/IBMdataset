s=list(input())
t=list(input())
l=[]
for i in range(len(s)-1):
    l.append(s[i])
    l.append(t[i])
if len(s)>len(t):
    l.append(s[len(s)-1])
else:
    l.append(s[len(s)-1])
    l.append(t[len(t)-1])

x=''.join(l)
print(x)
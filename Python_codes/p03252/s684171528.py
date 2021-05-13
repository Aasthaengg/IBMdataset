s=[ord(c) for c in input()]
t=[ord(c) for c in input()]
n=len(s)
st=[(s[i],t[i]) for i in range(n)]
st=sorted(st,key=lambda x:x[0])
s=[c for c,_ in st]
t=[c for _,c in st]

for i in range(n-1):
    if (s[i]==s[i+1]) ^ (t[i]==t[i+1]):
        print('No')
        exit(0)

st=sorted(st,key=lambda x:x[1])
s=[c for c,_ in st]
t=[c for _,c in st]

for i in range(n-1):
    if (s[i]==s[i+1]) ^ (t[i]==t[i+1]):
        print('No')
        exit(0)


print('Yes')
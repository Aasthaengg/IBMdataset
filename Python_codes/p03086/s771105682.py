S=input()
S+='S'
l=len(S)
x=['A','C','G','T']
a=0
m=0
for i in range(l):
    if S[i] in x:
        a+=1
    else:
        if a>m:
            m=a
        a=0
print(m)
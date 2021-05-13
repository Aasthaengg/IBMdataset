s=input()
A=[]
B=[]
for i in range(0,len(s)):
    if s[i]=='A':
        a=i
        break
S=list(reversed(s))
for j in range(0,len(S)):
    if S[j]=='Z':
        b=j
        break
print(len(s)-a-b)
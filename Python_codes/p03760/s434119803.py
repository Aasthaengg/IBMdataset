s=input()
t=input()
k=[]
for i in range(len(t)):
    k.append(s[i])
    k.append(t[i])
if len(s)>len(t):
    k.append(s[len(s)-1])
print("".join(k))

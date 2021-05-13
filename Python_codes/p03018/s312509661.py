so=input()

s=""

N=len(so)
i=0
while i<N:
    if so[i]=="A":
        s=s+"A"
        i+=1
    elif so[i:i+2]=="BC":
        s=s+"B"
        i+=2
    elif so[i]=="C" or so[i]=="B":
        s=s+"D"
        i+=1

L=len(s)
f=False
cnt=0
a=0
for i in range(L):
    if s[i]=="A":
        f=True
        a+=1
    elif f and s[i]=="B":
        cnt+=a
    elif s[i]=="D":
        f=False
        a=0
print(cnt)

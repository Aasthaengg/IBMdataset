s=input()

N=len(s)
g=0
p=0
w=0
l=0

for i in range(N):
    if g==p:
        g+=1
        if s[i]=="p":
            l+=1
    else:
        p+=1
        if s[i]=="g":
            w+=1
print(w-l)
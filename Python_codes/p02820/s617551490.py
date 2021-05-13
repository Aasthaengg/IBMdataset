n,k=map(int, input().split())
r,s,p=map(int, input().split())
t=input()

ten=0
te=[]

for i in range(k):
    if t[i]=="r":
        ten+=p
        te.append("p")
    elif t[i]=="s":
        ten+=r
        te.append("r")
    elif t[i]=="p":
        ten+=s
        te.append("s")

for i in range(k,len(t)):
    if t[i]=="r" and te[i-k]=="p":
        te.append("a")
    elif t[i]=="s" and te[i-k]=="r":
        te.append("a")
    elif t[i]=="p" and te[i-k]=="s":
        te.append("a")
    else:
        if t[i]=="r":
            ten+=p
            te.append("p")
        elif t[i]=="s":
            ten+=r
            te.append("r")
        elif t[i]=="p":
            ten+=s
            te.append("s")

print(ten)
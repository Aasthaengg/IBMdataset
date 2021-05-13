n=input()
L=[]
l=len(n)
for i in range(l):
    if n[i]=="1":
        L.append("9")
    else:
        L.append("1")
print("".join(L))
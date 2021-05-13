n=input()
s=[]
for i in range(3):
    if n[i] == "1":
        s.append(9)
    elif n[i] == "9":
        s.append(1)
    else:
        s.append(n[i])
print(*s,sep="")
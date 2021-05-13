n=input()

N=[]

for i in range(len(n)):
    if n[i]=="9":
        N.append("1")
    else:
        N.append("9")
print("".join(N))

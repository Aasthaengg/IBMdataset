N=input("")
N=N.split(" ")
K=int(N[1])
N=N[0]
s=str(input(""))
print(s[0:K-1]+s[K-1].lower()+s[K:])
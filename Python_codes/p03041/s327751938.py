N = input()
S = input()
N += "."
f = N.find(" ")
N1 =((N[0:f]))
K =(N[f+1:-1])
N1= int(N1)
S = S[0:N1+1]
S += "."
K= int(K)-1
s = (S[K:K+1])
s= s.lower()
print(S[0:K]+s+S[K+1:-1])
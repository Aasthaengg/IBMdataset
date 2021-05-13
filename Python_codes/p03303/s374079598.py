S = input()
N = input()
N = int(N)
A = ""
for i in range(0,len(S),N):
    A += S[i]

print (A)
N = int(input())
S = list(input())
L = len(S)

for i in range(L):
  S[i] = chr((ord(S[i])+N-65)%26+65)
  
print("".join(S))
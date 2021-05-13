# B String Palindrome

def check(S, N):
  for i in range((N-1)//2):
    if S[i] != S[-(1+i)]:
      print("No")
      exit()

def ot_check(S, N):
  for i in range(N//2):
    if S[i] != S[-(1+i)]:
      print("No")
      exit()

S = input()
N = len(S)

SS = S[0:(N-1)//2]
NN = len(SS)

SSS = S[((N+3)//2)-1:]
NNN = len(SSS)

check(S, N)
if len(SS)%2 == 0:
  ot_check(SS, NN)
else:
  check(SS, NN)
if len(SSS)%2 == 0:
  ot_check(SSS, NNN)
else:
  check(SSS, NNN)

print("Yes")



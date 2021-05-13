S=input()
M=1000
N=len(S)
for i in range(N-2):
  M=min(abs(753-int(S[i]+S[i+1]+S[i+2])),M)
print(M)
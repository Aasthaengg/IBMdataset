S=input()
ans=10**3
for i in range(len(S)-2):
  x=int(S[i])*100+int(S[i+1])*10+int(S[i+2])
  ans=min(abs(x-753),ans)
print(ans)
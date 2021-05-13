S=input()
T=input()

N_max = len(T)
for i in range(len(S)-len(T)+1):
  score=0
  for j in range(len(T)):
    if(S[i+j] != T[j]):
      score += 1
      
  N_max = min(score, N_max)
  
print(N_max)
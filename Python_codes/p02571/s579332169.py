S = input()
t = input()
neq = len(t)
for i in range(len(S)-len(t)+1):
  neq_temp = 0
  for j in range(len(t)):
    if S[i+j]!=t[j]:
      neq_temp += 1
  neq = min(neq,neq_temp)
print(neq)
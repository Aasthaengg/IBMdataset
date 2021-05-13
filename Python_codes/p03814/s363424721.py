S=[x for x in input()]
T=S[::-1]
start=0
end=0
for i in range(len(S)):
  if S[i]=='A':
    start=i
    break
for i in range(len(T)):
  if T[i]=='Z':
    end=i
    break
    
print(len(S)-end-start)
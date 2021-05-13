S=input()
start=0
end=len(S)-1
for i in range(len(S)):
  if S[i]=="A":
    start=i
    break
S=S[::-1]
for i in range(len(S)):
  if S[i]=="Z":
    end = len(S)-i
    break
print(end-start)
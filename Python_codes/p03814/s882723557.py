S=input()
start=0
last=0
for i in range(len(S)):
    if S[i]=='A':
        start=i
        break

for j in range(1,len(S)+1):
    if S[-j]=='Z':
        last=len(S)-j
        break
    
print(last-start+1)
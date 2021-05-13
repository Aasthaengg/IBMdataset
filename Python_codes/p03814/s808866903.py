S = input()
f=0
l=0
for i in range(len(S)):
    if(S[i] =="A"):
        f = i+1
        break
for j in range(len(S)-1,0,-1):
    if(S[j] == "Z"):
        l = j+1
        break
print(l-f+1)
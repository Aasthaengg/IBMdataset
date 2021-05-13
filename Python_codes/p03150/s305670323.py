S=input()
T="keyence"
if S[:7]==T:
    print("YES")
    exit()
for i in range(len(S)-1):
    for j in range(i,len(S)):
        if S[:i]+S[j:]==T:
            print("YES")
            exit()
print("NO")
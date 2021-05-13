S=input()
ans = 0
for i in range(1,len(S)+1):
    for j in range(0,len(S)-i+1):
        if all([c in ["A","T","G","C"] for c in S[j:j+i]]):
            ans = i
print(ans)
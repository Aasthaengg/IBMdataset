small=list()
S=list(input())
for i in range(len(S)-2):
    small.append(abs(int(S[i]+S[i+1]+S[i+2])-753))
print(min(small))
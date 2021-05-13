S, T = [input() for i in range(2)]
ans = 0

for i in range(len(S)-len(T)+1):
    diff = 0

    for j in range(len(T)):
        if T[j] == S[i+j]:
            diff +=1
    ans = max(ans, diff)

print(len(T)-ans)
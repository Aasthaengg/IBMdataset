S=str(input())
T=str(input())


U=[0]*(len(S)-len(T)+1)
c=[0]*(len(S)-len(T)+1)
for j in range(len(S)-len(T)+1):
    U[j]=S[j:j+len(T)]
    for i in range(len(T)):
        if U[j][i]==T[i] :c[j]=c[j]+1

print(len(T)-max(c))
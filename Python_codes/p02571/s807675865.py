S=input()
T=input()
A=[]
for i in range(len(S)-len(T)+1):
    ans = 0
    for j in range(len(T)):
        if S[i+j]!=T[j]:
            ans += 1
    A.append(ans)

print(min(A))


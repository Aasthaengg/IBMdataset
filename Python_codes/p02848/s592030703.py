#B
N=int(input())
S=input()

alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans=""
for i in range(len(S)):
    for j in range(26):
        if alpha[j]==S[i]:
            index=(j+N)%26
            ans+=alpha[index]
            break
print(ans)
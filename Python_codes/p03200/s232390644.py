S = list(input())
c = 0
Bc = 0
for i in range(len(S)):
    if S[i] == 'B':
        Bc+=1
    else:
        c += Bc
print(c)

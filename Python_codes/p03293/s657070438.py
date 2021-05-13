S=list(str(input()))
T=list(str(input()))
for i in range(len(S)):
    S.append(S[i])
j=0
while j+len(T)<=len(S):
    if S[j:j+len(T)]==T:
        print('Yes')
        exit()
    j+=1

print('No')
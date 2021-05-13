
S=input()
T=input()
check=[]
for i in range(len(S)-len(T)+1):
    check.append(0)
    for j,tt in enumerate(T):
        if tt==S[i+j]:
            check[i]+=1
# print(check)
check.append(0)
# print(check)
print(len(T)-max(check))
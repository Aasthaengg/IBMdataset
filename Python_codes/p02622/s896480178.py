S=input()
T=input()
count=0
for j in range(0,len(T)):
    if S[j]==T[j]:
        count+=1   
print(len(T)-count)
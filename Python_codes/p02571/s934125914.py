S=input()
T=input()
a=0
for i in range(0,len(S)-len(T)+1):
    count=0
    for j in range(0,len(T)):
        if S[i+j]==T[j]:
            count+=1
    if a<=count:
        a=count
print(len(T)-a)
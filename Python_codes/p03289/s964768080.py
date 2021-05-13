S=str(input())
cnt=0
for i in range(2,len(S)-1):
    if S[i] =='C':
        cnt+=1
if cnt==1:
    if S[0]=='A':
        T = S.replace("C","").replace("A","")
        if T.islower():
            print("AC")
            exit()
print("WA")
S=str(input())
cnt=0
T = S.replace("C","").replace("A","")
for i in range(2,len(S)-1):
    if S[i] =='C':cnt+=1
if cnt==1 and S[0]=='A' and T.islower():
    print("AC")
    exit()
print("WA")
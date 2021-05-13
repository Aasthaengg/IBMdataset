N,K,C=map(int,input().split())
S=input()

mae=[]
rest=0
work=0
for i in range(len(S)):
    if S[i]=='o' and rest==0:
        mae.append(i)
        rest=C
        work+=1
    else:
        rest=max(rest-1,0)
    if work==K:
        break
        
usiro=[]
rest=0
work=0
S=S[::-1]
for i in range(len(S)):
    if S[i]=='o' and rest==0:
        usiro.append(len(S)-i-1)
        rest=C
        work+=1
    else:
        rest=max(rest-1,0)
    if work==K:
        break

usiro=usiro[::-1]

for i in range(K):
    if mae[i]==usiro[i]:
        print(mae[i]+1)
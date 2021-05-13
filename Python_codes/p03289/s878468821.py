S=input()
Sdash=[]
for i in range(2,len(S)-1):
    Sdash.append(S[i])
a=0
for i in range(len(S)):
    if S[i].islower()==True:
        a+=1
if S[0]=='A' and Sdash.count('C')==1 and a==len(S)-2:
    print('AC')
else:
    print('WA')
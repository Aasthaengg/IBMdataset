S=input()
res=0
cnt=0
if S[0]!='A':
    print('WA')
    exit()
for i in range(2,len(S)-1):
    if S[i]=='C' and cnt==0:
        cnt+=1
        res=1
    elif S[i]=='C' and cnt==1:
        res=0
for i in range(len(S)):
    if S[i]!='A' and S[i]!='C' and S[i].isupper() == True:
        print('WA')
        exit()
if res==0:
    print('WA')
else:
    print('AC')
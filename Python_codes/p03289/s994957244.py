

S=str(input())
temp=0
j=0
if S[0]!='A':
    print('WA')
    exit()
for i in range(2,len(S)-1):
    if S[i]=='C':
        temp+=1
        j=i
if temp!=1:
    print('WA')
    exit()
for i in range(len(S)):
    if i!=0 and i!=j:
        if S[i].isupper():
            print('WA')
            exit()
print('AC') 
exit()    
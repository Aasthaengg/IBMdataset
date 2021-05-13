S=input()
chk = [False, False, False]
if S[0]=="A":
    chk[0]=True

ind = 0
for i in range(2, len(S)-1):
    if S[i]=="C":
        chk[1]=True
        ind=i

chk[2]=True
for i in range(len(S)):
    if i==ind or i==0:
        continue
    if S[i].isupper():
        chk[2]=False

if chk[0] and chk[1] and chk[2]:
    print("AC")
else:
    print("WA")
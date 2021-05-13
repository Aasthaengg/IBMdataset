a=0
S=input()
T=input()
l=len(S)
for i in range(l):
    if S[i]!=T[i]:
        a=1
        break
if a==0:
    print('Yes')
else:
    print('No')
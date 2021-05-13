N=int(input())
count=0
LastA=0
FirstB=0
LA=0
for i in range(0,N):
    f=input()
    count=count+f.count('AB')
    if f[0]=='B' and f[-1]=='A':
        LA=LA+1
    elif f[0]=='B':
        FirstB=FirstB+1
    elif f[-1]=='A':
        LastA=LastA+1
count=count+LA
if LastA==0 and FirstB==0 and LA!=0:
    count=count-1
elif FirstB>=LastA:
    count=count+LastA
else:
    count=count+FirstB
print(count)
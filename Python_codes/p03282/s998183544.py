s=input()
k=int(input())

cntone=0
while len(s)>cntone and s[cntone]=='1':
    cntone+=1

if k>cntone:
    print(s[cntone])
else:
    print(s[0])

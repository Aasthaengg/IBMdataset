n=int(input())

headB=0
tailA=0
middleAB=0
ck=0
for _ in range(n):
    s=list(input())

    for i in range(1,len(s)):
        if s[i-1]=="A" and s[i]=="B":
            middleAB+=1
    if s[0]=="B":
        headB+=1
    if s[-1]=="A":
        tailA+=1
    if s[0]=="B" and s[-1]=="A":
        ck+=1

#BA
#BC
#CA みたいなケースは2になる

#BA
#BA　みたいなケースは１になる

if ck>0 and ck==tailA and ck==headB:
    print(middleAB+min(headB,tailA)-1)
else:
    print(middleAB+min(headB,tailA))


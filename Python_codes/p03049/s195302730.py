N=int(input())
s=[input() for _ in range(N)]
abcount=0
righta=0
leftb=0
bothab=0
buf=""
for i in range(N):
    buf=s[i]
    l=len(buf)
    if (buf[0]=="B")and(buf[l-1]=="A"):
        bothab=bothab+1
    elif (buf[0]=="B"):
        leftb=leftb+1
    elif (buf[l-1]=="A"):
        righta=righta+1
    for j in range(l-1):
        if (buf[j]=="A")and(buf[j+1]=="B"):
            abcount=abcount+1
abcount=abcount+max(0,bothab-1)
#print(bothab,righta,leftb,abcount)
if (righta>0)and(bothab>0):
    abcount=abcount+1
    righta=righta-1
if (leftb>0)and(bothab>0):
    abcount=abcount+1
    leftb=leftb-1
abcount=abcount+min(righta,leftb)

'''
abcount=abcount+min(bothab,righta,leftb)*2


if min(bothab,righta,leftb)==bothab:
    leftb=leftb-bothab
    righta=righta-bothab
    abcount=abcount+min(leftb,righta)
elif min(bothab,righta,leftb)==righta:
    bothab=bothab-righta
    leftb=leftb-righta
    abcount=abcount+max(0,bothab-1)
    if leftb>0:
        abcount=abcount+1
else:
    bothab=bothab-leftb
    righta=righta-leftb
    abcount=abcount+max(0,bothab-1)
    if righta>0:
        abcount=abcount+1
'''
print(abcount)

a1=input()
a2=input()
A1=list(a1)
A2=list(a2)
i=0
for x in A1:
    if x!='C' and x!='S' and x!='R':
        A1.remove(x)
for x in A2:
    if x!='C' and x!='S' and x!='R':
        A2.remove(x)
if len(A1)==len(A2)==3:   
    if A1[0]==A2[0]:
        i+=1
    if A1[1]==A2[1]:
        i+=1
    if A1[2]==A2[2]:
        i+=1
    print(i)
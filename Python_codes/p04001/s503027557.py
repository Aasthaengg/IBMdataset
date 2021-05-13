import sys
S=input()
S_seq=[]
for i in S:
    S_seq.append(i)
if(len(S_seq)==1):
    print(int(S))
    sys.exit()
separate=[]
for i in range(len(S_seq)-1):
    a=[]
    if(i==0):
        a.append("*")
        a.append("_")
    else:
        for j in separate:
            a.append(j+"*")
            a.append(j+"_")
    separate=a

separated=[]
for i in separate:
    a=[]
    for j in i:
        a.append(j)
    separated.append(a)

pre_calculated=[]
for i in separated:
    a=[]
    for j in range(len(S_seq)-1):
        a.append(S_seq[j])
        if(i[j]=="*"):
            a.append("+")
        elif(i[j]=="_"):
            continue
    a.append(S_seq[-1])
    pre_calculated.append(a)

sumation=0
for i in pre_calculated:
    number=[]
    for j in range(len(i)):
        new_number=[]
        if(j==len(i)-1):
            for k in number:
                sumation+=k*10
            sumation+=int(i[j])
        elif(i[j]=="+"):
            for k in number:
                sumation+=k
            number=[]
        else:
            for k in number:
                new_number.append(k*10)
            new_number.append(int(i[j]))
        
        number=new_number
print(sumation)

    

list_m=[]
list_f=[]
list_r=[]
while True:
    m,f,r=map(int,input().split())
    if m==-1 and f==-1 and r==-1:
        break
    else:
        list_m.append(m)
        list_f.append(f)
        list_r.append(r)

for i in range(len(list_m)):
    M=list_m[i]
    F=list_f[i]
    R=list_r[i]
    score=M+F
    if M==-1 or F==-1:
        grade="F"
    elif score>=80:
        grade="A"
    elif 65<= score <80:
        grade="B"
    elif 50<= score <65:
        grade="C"
    elif 30<= score <50:
        if R>=50:
            grade="C"
        else:
            grade="D"
    else:
        grade="F"
    print(grade)
      

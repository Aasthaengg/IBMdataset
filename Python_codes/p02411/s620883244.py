a=[]
w=""
while(w!="-1 -1 -1"):
    w=input()
    a.append(w)
a.pop()
for st in a:
    s=st.split()
    m=int(s[0])
    f=int(s[1])
    r=int(s[2])
    if (m==-1 or f==-1):
        print("F")
    elif (m+f>=80):
        print("A")
    elif(m+f>=65):
        print("B")
    elif(m+f>=50):
        print("C")
    elif(m+f>=30 and r>=50):
        print("C")
    elif(m+f>=30 and r<50):
        print("D")
    else:
        print("F")
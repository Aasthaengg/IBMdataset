m = []
f = []
r = []
while(True):
    M,F,R=map(int,input().split())
    if M == -1 and F == -1 and R == -1:
        break
    else:
        m.append(M)
        f.append(F)
        r.append(R)
for i in range(len(m)):
    score = m[i]+f[i]
    if (m[i] == -1 or f[i] ==-1) or score<30:
        print("F")
    elif score>=80:
        print("A")
    elif 65<=score<80:
        print("B")
    elif 50<=score<65:
        print("C")
    elif 30<=score<50 and r[i]>=50:
        print("C")
    elif 30<=score<50:
        print("D")

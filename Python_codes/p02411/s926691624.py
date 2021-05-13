s=[]
while True:
    m,f,r = map(int, input().split())
    if m==-1 and f==-1 and r==-1:
        break

    if m==-1 or f==-1:
        s.append('F')
        continue
    elif m+f>=80:
        s.append('A')
        continue
    elif m+f>=65 and m+f<80:
        s.append('B')
        continue
    elif m+f>=50 and m+f<65:
        s.append('C')
        continue
    elif m+f>=30 and m+f<50:
        if r>=50:
            s.append('C')
        else:
            s.append('D')
        continue
    elif m+f<30:
        s.append('F')

for i in range(len(s)):
    print(s[i])



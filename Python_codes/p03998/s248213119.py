S=list(input() for i in range(3))
i=0
while True:
    if S[i]=='':
        print(chr(i+65))
        exit()
    c=S[i][0]
    S[i]=S[i][1:]
    i=ord(c)-97
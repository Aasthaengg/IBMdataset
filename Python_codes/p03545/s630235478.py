s=input()
for i in range(2**3):
    t=s[0]
    for j in range(3):
        if i%2:t+='+'
        else:t+='-'
        i//=2
        t+=s[j+1]
    if eval(t+'==7'):
        print(t+'=7')
        exit()
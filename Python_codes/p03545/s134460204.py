S=input()

for i in range(2**3):
    t=S[0]
    for j in range(3):
        if i & (1<<j):
            t+='+'
        else:
            t+='-'
        t+=S[j+1]
    if eval(t)==7:
        break
print(t+'=7')
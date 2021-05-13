n=input()
N=list(n)
for i in range(3):
    if(N[i]=='1'):
        N[i]='9'
    elif(N[i]=='9'):
        N[i]='1'
n=''.join(N)
print(n)

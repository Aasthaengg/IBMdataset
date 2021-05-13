# your code goes here
#polland
def nu(x):
    if x=="+" or x=="-" or x=="*":
        return 0
    else:
        return 1
def c(a,b,l):
    if l=="+":
        d=a+b
    elif l=="-":
        d=a-b
    else:
        d=a*b
    return d
F=[i for i in input().split()]
i=0
S=[]
while i<len(F):
    if nu(F[i])==0:
        S[-2]=c(S[-2],S[-1],F[i])
        S.pop(-1)
    else:
        S.append(int(F[i]))
    i+=1
print(S[0])
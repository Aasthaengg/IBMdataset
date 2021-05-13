def f(N):
    if N==1:
        return [[0]]

    X=f(N-1)
    Y=[]
    for x in X:
        k=max(x)
        for a in range(min(k+2,10)):
            Y.append(x+[a])
    return Y

T={0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"j"}
N=int(input())

for a in f(N):
    S=""
    for x in a:
        S+=T[x]
    print(S)

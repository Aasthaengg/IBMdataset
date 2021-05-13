S=int(input())
a=[]

for i in range(1, 1000001):
    if S in a:
        print(i)
        break
    else:
        a.append(S)
        if S%2==0:
            S=S/2
        else:
            S=3*S+1

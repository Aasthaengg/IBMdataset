T=list(input())
N=len(T)
i=0
while i<N-1:
    if i<N-2:
        if T[i]=="D":
            if (T[i+1]=="?")and((T[i+2]=="?")or(T[i+2]=="D")):
                T[i+1]="P"
                T[i+2]="D"
                i=i+2
            elif (T[i+1]=="?"):
                T[i+1]="D"
                i=i+1
            else:
                i=i+1
        elif T[i]=="P":
            if (T[i+1]=="?"):
                T[i+1]="D"
                i=i+1
            else:
                i=i+1
        else:
            if T[i+1]=="P":
                T[i]="D"
                i=i+1
            else:
                T[i]="P"
                T[i+1]="D"
                i=i+1
    if i==N-2:
        if T[i]=="?":
            if (T[i+1]=="D")or(T[i+1]=="?"):
                T[i]="P"
                T[i+1]="D"
                i=i+1
            else:
                T[i]="D"
                i=i+1
        elif T[i+1]=="?":
            T[i+1]="D"
            i=i+1
        else:
            i=i+1
    #print(i,T)
    #input()
if (len(T)==1)and(T[0]=="?"):
    T[0]="D"
print("".join(T))

A=input().split()
l=len(A)
x=[]

for i in range(l):
    
    if A[i]=="+":
        a=x.pop() #先頭の文字を消して返す
        b=x.pop()
        x.append(int(b)+int(a))

    elif A[i]=="-":
        a=x.pop()
        b=x.pop()
        x.append(int(b)-int(a))

    elif A[i]=="*":
        a=x.pop()
        b=x.pop()
        x.append(int(b)*int(a))

    else:
        x.append(A[i])

print(x[0])

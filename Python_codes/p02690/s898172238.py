# A^5-B^5=(B+d)^5-B^5

X=int(input())

div=[1,X]

for i in range(2,X):
    if X%i==0:
        div.append(i)
        div.append(X//i)
    if i*i>=X:
        break

for d in div:
    for j in range(-100000,100000):
        A=j+d
        B=j
        if A**5-B**5==X:
            print(str(A)+" "+str(B))
            exit(0)
            

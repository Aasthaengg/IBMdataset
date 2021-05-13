x = int(input())

C=[]
for i in range(10*100) :
    C.append(i**5)

# print( C )

for j in range(len(C)):
    for i in range(len(C)):
        if C[j]-C[i]==x :
            print( j, i )
            exit()
        elif C[j]+C[i]==x :
            print( j, 0-(i) )
            exit()




A=[]
S=input()
if len(S)==3:
    for i in S[::-1]:
        A.append(i)
    print("{}{}{}".format(A[0],A[1],A[2]))
else:
    print(S)
A=input()
B=input()
flag="EQUAL"

if len(A)!=len(B):
    if(len(A)>len(B)):
        print("GREATER")
    else:
        print("LESS")
else:
    for i in range(len(A)):
        if A[i] > B[i]:
            flag="GREATER"
            break
            
        elif A[i] < B[i]:
            flag="LESS"
            break
    print(flag)
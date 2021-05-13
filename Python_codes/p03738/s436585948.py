A=input()
B=input()

if len(A)<len(B):
    print("LESS")
elif len(A)>len(B):
    print("GREATER")
else:
    cnt=0
    for i in range(len(A)):
        if A[i]>B[i]:
            print("GREATER")
            break
        elif A[i]<B[i]:
            print("LESS")
            break
        else:
            cnt+=1
    if cnt==len(A):
        print("EQUAL")

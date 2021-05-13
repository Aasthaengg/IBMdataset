while True:
    C=input()
    if C=='-':
        break
    R=int(input())
    for i in range(R):
        h=int(input())
        RV=[]
        RV.append(C[h:])
        RV.append(C[:h])
        C=''.join(RV)
    print(C)    

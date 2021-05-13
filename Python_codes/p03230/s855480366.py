N=int(input())
if N==1:
    print("Yes")
    print(2)
    print(1,1)
    print(1,1)
    exit()

for i in range(2,1000):
    if i*(i+1)//2==N:
        print("Yes")
        print(i+1)
        L=[]
        cnt=1
        for j in range(i+1):
            l=[]
            for k in range(len(L)):
                l.append(L[k][len(L)-1])
            while len(l)<i:
                l.append(cnt)
                cnt+=1
            L.append(l)
        for i in range(len(L)):
            print(len(L[i]),*L[i])
        exit()
        
    elif i*(i+1)//2>N:
        print("No")
        exit()
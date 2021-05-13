import math
N=int(input())

if N==2:
    print(N)
    exit()
while True:
    maxi=int(math.sqrt(N))+1
    test=[i for i in range(maxi)]
    for i in range(2,maxi):
        if test[i]!=-1:
            if N%test[i]!=0:
                j=i
                while j<maxi:
                    test[j]=-1
                    j+=i
            else:
                break
        if i==maxi-1:
            print(N)
            exit()
    N+=1
from itertools import combinations
N = int(input())
if N==1:
    print("Yes")
    print(2)
    print(1,1)
    print(1,1)
elif N==2:
    print("No")
elif N==3:
    print("Yes")
    print(3)
    print(2,1,2)
    print(2,1,3)
    print(2,2,3)
else:
    flg = 0
    for i in range(4,int((3*N)**0.5)+2):
        if N==(i*(i-1))//2:
            flg=1
            K = i
            break
    if flg==0:
        print("No")
    else:
        S = {i:[] for i in range(K)}
        for j,x in enumerate(combinations(range(K),2)):
            j += 1
            i0,i1 = x[0],x[1]
            S[i0].append(j)
            S[i1].append(j)
        print("Yes")
        print(K)
        for i in range(K):
            print(len(S[i]),*S[i])
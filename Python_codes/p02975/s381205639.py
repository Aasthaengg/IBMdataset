N = int(input())
A = list(map(int,input().split()))
C = {}
for i in range(N):
    if A[i] not in C:
        C[A[i]] = 0
    C[A[i]] += 1
if len(C)>3:
    print("No")
else:
    if N%3==0:
        if 0 in C:
            if len(C)==1:
                print("Yes")
            elif len(C)==2:
                if C[0]==N//3:
                    print("Yes")
                else:
                    print("No")
            else:
                print("No")
        else:
            if len(C)!=3:
                print("No")
            else:
                flag = 0
                for a in C:
                    if C[a]!=N//3:
                        flag = 1
                        break
                if flag==0:
                    C = list(C.keys())
                    if C[0]^C[1]==C[2]:
                        print("Yes")
                    else:
                        print("No")
                else:
                    print("No")
    else:
        if len(C)==1 and 0 in C:
            print("Yes")
        else:
            print("No")
N=int(input())
S=input()
if N%2==1:
    print("No")
else:
    for i in range(int(N/2)):
        if S[i]!=S[int(N/2)+i]:
            print("No")
            break
    else:
        print("Yes")
N=int(input())
A=list(map(int,input().split()))
if A.count(0)==N:
    print("Yes")
elif N%3!=0:
    print("No")
elif len(set(A))==2:
    if 0 in set(A):
        if A.count(0)==N/3:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
elif len(set(A))==3:
    xor=0
    for a in set(A):
        if A.count(a)==N/3:
            xor^=a
        else:
            print("No")
            exit()
    if xor==0:
        print("Yes")
    else:
        print("No")
else:
    print("No")
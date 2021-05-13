N,A,B,C,D=map(int,input().split())
S=list(input())

if A<B<C<D:
    a=True
    for i in range(A-1,D-2):
        if S[i]==S[i+1]=="#":
            print("No")
            a=False
            break
    if a==True:
        print("Yes")
elif A<C<B<D:
    a=True
    for i in range(A-1,C-2):
        if S[i]==S[i+1]=="#":
            print("No")
            a=False
            break
    if a==True:
        for i in range(B-1,D-2):
            if S[i]==S[i+1]=="#":
                print("No")
                a=False
                break
    if a==True:
        print("Yes")
elif A<B<D<C:
    a=True
    for i in range(A-1,C-2):
        if S[i]==S[i+1]=="#":
            b=True
            a=False
            break
    if a==True:
        b=True
        for i in range(B-2,D-2+1):
            if S[i]==S[i+1]==S[i+2]:
                b=False
                break
    if b==False:
        print("Yes")
    elif b==True:
        print("No")
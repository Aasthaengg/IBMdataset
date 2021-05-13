N,A,B=map(int,input().split())
while True:
    if A+1<B:
        A+=1
    elif 1<A:
        A-=1
    else:
        print("Borys")
        break
    if A<B-1:
        B-=1
    elif B<N:
        B+=1
    else:
        print("Alice")
        break
A,B = map(int,input().split())

if A<1 or 100<A or B<1 or 100<B:
    print("One more time!")
else:
    print(A * B)
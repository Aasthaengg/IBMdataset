N, A, B = list(map(int,input().split()))

space = abs(B - A )

if space % 2 ==0:
    print("Alice")
else :
    print("Borys")
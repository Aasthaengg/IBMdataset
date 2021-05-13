A = input().strip()
B = input().strip()
if len(A)>len(B):
    print("GREATER")
elif len(A)<len(B):
    print("LESS")
else:
    if A<B:
        print("LESS")
    elif A>B:
        print("GREATER")
    else:
        print("EQUAL")
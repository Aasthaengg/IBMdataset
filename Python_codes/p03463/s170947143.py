N,A,B = map(int, input().split())

if A % 2 == 0 and B % 2 == 0:
    print("Alice")
elif A % 2 == 0 and B % 2 != 0:
    print("Borys")
elif A % 2 != 0 and B % 2 == 0:
    print("Borys")
elif A % 2 != 0 and B % 2 != 0:
    print("Alice")
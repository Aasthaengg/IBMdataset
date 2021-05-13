A, B = map(int,input().split())
if A > 12:
    print(B)
elif A > 5 and A < 13:
    print(int(B/2))
elif A < 6:
    print(0)
A, B = map(int,input().split())

if B <= 1:
    print(0)

elif A >= B:
    print(1)

elif (B-A) % (A-1) == 0:
    print((B-A) // (A-1) + 1)

else:
    print((B-A) // (A-1) + 2)
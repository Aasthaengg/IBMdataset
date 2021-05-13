A,B,C = map(int, input().split())

if B / A >= C:
    print(C)

elif 1 <= B / A < C:
    print(B //A)

else:
    print(0)
   
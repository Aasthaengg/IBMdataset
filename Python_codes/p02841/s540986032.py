M1, D1 = tuple(map(int, input().split()))
M2, D2 = tuple(map(int, input().split()))
M1 = 1 if M1 + 1 > 12 else M1 + 1
if M1 == M2 and D2 == 1:
    print(1)
else:
    print(0)

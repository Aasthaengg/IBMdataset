#Parking
N, A, B = map(int, input().split())
plan1 = N * A
plan2 = B
if plan1 >= plan2:
    print(plan2)
else:
    print(plan1)
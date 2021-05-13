A, B, C = map(int, input().split())

AB = A+B
BC = B+C
CA = C+A

if AB==C or BC==A or CA==B:
    print("Yes")
else:
    print("No")

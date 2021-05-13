N = int(input())
SqN = 1
while True:
    if SqN**2>N:
        print((SqN-1)**2)
        break
    SqN += 1
A,B = map(int, input().split())

AaddB = (A+B)
AminuseB = (A-B)
AtimseB = (A*B)

print(max(AaddB,AminuseB,AtimseB))
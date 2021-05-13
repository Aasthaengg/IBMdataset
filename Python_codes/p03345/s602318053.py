A, B, C, K = [int(s) for s in input().split(' ')]
n = K % 2
ANS = (A-B) * (-1) ** n
print(ANS)
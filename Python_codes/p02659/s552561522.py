A,B = input().split()

A = int(A)
B1,B2 = B.split(".")
answer = A * (int(B1) * 100 + int(B2))

print(answer // 100)
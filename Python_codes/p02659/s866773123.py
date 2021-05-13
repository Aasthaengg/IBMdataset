AB = input().split()
A = int(AB[0])
B = AB[1].split('.')
B = int(B[0]) * 100 + int(B[1])

print(A * B // 100)


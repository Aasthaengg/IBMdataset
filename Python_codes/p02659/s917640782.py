A, B = input().split()
A = int(A)
B1, B2 = map(int, B.split('.'))
ans = A * B1 + A * B2 // 100
print(ans)
A, B, C = map(int, input().split())

C_eat = min(A+B+1,C)

print(B + C_eat)
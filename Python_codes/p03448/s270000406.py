A = int(input())
B = int(input())
C = int(input())
X = int(input())
answer = 0
for i in range(min(A, X // 500) + 1):
    for j in range(min(B, (X - i * 500) // 100) + 1):
        if X - 500 * i - 100 * j <= 50 * C:
            answer += 1
print(answer)

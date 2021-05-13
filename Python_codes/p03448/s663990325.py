A = int(input())
B = int(input())
C = int(input())
X = int(input())

k = 0
for a in range(min([A, X // 500]) + 1):
    Y = X - 500 * a
    for b in range(min([B, Y // 100]) + 1):
        k += (Y - 100 * b) // 50 <= C

print(k)

A = int(input())
B = int(input())
C = int(input())
X = int(input())
res = 0
for a500 in range(A + 1):
    for b100 in range(B + 1):
        for c50 in range(C + 1):
            if a500 * 500 + b100 * 100 + c50 * 50 == X:
                res += 1
print(res)
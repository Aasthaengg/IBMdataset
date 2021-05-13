n = int(input())
A, B = [], []
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
result = 0
for a, b in zip(A[::-1], B[::-1]):
    piyo = (a+result) % b
    if piyo == 0:
        continue
    result += b - piyo
print(result)
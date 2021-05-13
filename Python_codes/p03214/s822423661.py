n = int(input())
A = list(map(int, input().split()))

mean = sum(A) / n

B = []
for i in A:
    B.append(abs(i - mean))
print(B.index(min(B)))
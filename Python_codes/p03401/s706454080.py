N = int(input())
A = list(map(int, input().split()))

A = [0] + A + [0] # 数はN+2こ
kane = []
for i in range(1, N+2):
    kane.append(abs(A[i] - A[i-1]))
skane = sum(kane)

for i in range(1, N+1):
    print(skane - kane[i-1] - kane[i] + abs(A[i+1] - A[i-1]))
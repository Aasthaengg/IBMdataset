n = int(input())
a = [0] + list(map(int, input().split())) + [0]
A = [abs(a[i] - a[i + 1]) for i in range(n + 1)]
total = sum(A)

for i in range(n):
    print(total + abs(a[i + 2] - a[i]) - A[i] - A[i + 1])
    

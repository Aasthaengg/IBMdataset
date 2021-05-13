n = int(input())
A = list(map(int, input().split()))
t = 0
for i in range(n):
    if i+1 == A[A[i] - 1]:
        t += 1
print(t//2)
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
satisfaction = 0
last_dish = 10000

for i in range(N):
    satisfaction += B[A[i]-1]
    if A[i] - last_dish == 1:
        satisfaction += C[last_dish-1]
    last_dish = A[i]

print(satisfaction)

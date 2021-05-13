N = int(input())
A = input()
B = input()
C = input()
answer = 0

for i in range(N):
    answer += len({A[i], B[i], C[i]}) - 1

print(answer)
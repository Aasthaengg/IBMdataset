N = int(input())
A = list(map(int, input().split()))

answer = 0
for i, a in enumerate(A, 1):
    if i % 2 and a % 2:
        answer += 1

print(answer)
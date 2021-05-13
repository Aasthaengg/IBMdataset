N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

answer = 0
for i in (range(1, N+1)):
  answer += A[i*2 - 1]

print(str(answer))
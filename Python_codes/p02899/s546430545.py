n = int(input())
an = [int(num) for num in input().split()]

answer = [0 for _ in range(n)]
for index in range(n):
  answer[an[index] - 1] = str(index + 1)

print(" ".join(answer))
n = int(input())

numbers = list(map(int, input().rstrip(" ").split(" ")))

answer = 0
for i in range(0,n,2):
  if numbers[i] % 2 == 1:
    answer += 1

print(answer)
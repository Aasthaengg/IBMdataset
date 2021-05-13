n = int(input())
arr = list(map(int, input().split()))

answer = 0
for num1 in range(0, len(arr) - 1):
    for num2 in range(num1+1, len(arr)):
        answer += (arr[num1] * arr[num2])

print(answer)
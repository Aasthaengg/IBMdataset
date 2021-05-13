n = int(input())
arr = list(map(int, input().split()))

answer = 0
maximum = arr[0]
for index in range(1, len(arr)):
    maximum = max(maximum, arr[index])
    answer += abs(maximum - arr[index])

print(answer)
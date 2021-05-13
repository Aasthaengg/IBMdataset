n = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
answer = [0, 0]
for index in range(len(arr)):
    answer[index % 2] += arr[index]
print(answer[0] - answer[1])
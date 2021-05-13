n = int(input())
arr = list(map(int, input().split()))

answer = 0
while True:
    for index in range(len(arr)):
        if arr[index] % 2 != 0:
            print(answer)
            exit()
        arr[index] //= 2
    answer += 1
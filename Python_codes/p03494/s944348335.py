N = int(input())
nums = list(map(int, input().split()))

cnt = 0

while True:
    for i in range(N):
        if nums[i] % 2 == 1:
            result = "Odd"
            break
        else:
            result = "Even"
            nums[i] /= 2
    if result == "Odd": break
    cnt += 1
print(cnt)

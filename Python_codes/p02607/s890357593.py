n = int(input())
cnt = 0
arr = [int(x) for x in input().split()]
for i in range(0, len(arr), 2):
    if arr[i] % 2 != 0:
        cnt += 1

print(cnt)

N = int(input())
arr = list(map(int, input().split()))

bunbo = 0
for i in range(len(arr)):
    bunbo += 1/arr[i]

print(1/bunbo)
n = int(input())
a = list(map(int, input().split()))

arr = [0]*n
for i in a:
    arr[i-1] += 1

[print(i) for i in arr]
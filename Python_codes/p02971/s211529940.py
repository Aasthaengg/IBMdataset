N = int(input())
arr = [int(input()) for _ in range(N)]
arr2 = sorted(arr)
for i in range(N):
    print(arr2[-2] if arr[i] == arr2[-1] else arr2[-1])
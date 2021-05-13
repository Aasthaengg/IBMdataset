def solve(arr):
    for i in range(len(arr)):
        if arr[i]==0:
            return i+1

arr = list(map(int,input().split()))

print(solve(arr))
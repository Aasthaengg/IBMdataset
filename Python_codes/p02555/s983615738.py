S = int(input())
arr = [0]*(S+1)
MOD = 10**9 + 7

arr[0] = 1
for i in range(3,S+1):
    for j in range(i-3+1):
        arr[i] += arr[j]
        arr[i] = arr[i]%MOD

print(arr[S])
n, k = map(int, input().split())

total = 1
A = list(map(int, input().split()))

for i in range(n):
    if i < k:
        continue
    else:
        if A[i-k] < A[i]:
            print("Yes")
        else:
            print("No")
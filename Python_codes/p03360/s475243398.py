arr = []

A, B, C = map(int, input().split())
K = int(input())

arr.append(A)
arr.append(B)
arr.append(C)

arr = sorted(arr)
for i in range(0,K):
  arr[2]=2*arr[2]
print(sum(arr))
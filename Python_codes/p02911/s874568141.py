N, K, Q = map(int, input().split())
arr = [0] * N
for i in range(Q):
  q = int(input())
  arr[q-1] += 1
for i in range(N):
  if K - Q + arr[i] > 0:
    print("Yes")
  else:
    print("No")
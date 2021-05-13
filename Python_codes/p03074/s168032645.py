# https://atcoder.jp/contests/abc124/tasks/abc124_d

N, K = map(int, input().split())
S = input()
arr = []
prev = '1'
length = 0
for c in S:
  if prev != c:
    arr.append(length)
    length = 0
  length += 1
  prev = c
arr.append(length)
if S[-1] == '0':
  arr.append(0)

arr = [0] + arr
for i in range(len(arr) - 1):
    arr[i + 1] += arr[i]

L = K * 2 + 1
if L >= len(arr):
  print(N)
  exit()
ans = 0
for i in range(0, len(arr) - L, 2):
    t = arr[i + L] - arr[i]
    ans = max(ans, t)
print(ans)

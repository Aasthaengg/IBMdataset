from bisect import *
n,m,k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Aの累積和を保存しておく
# 各Aの要素について、Bが何冊読めるか二分探索する。
# 計算量: AlogB
A.insert(0, 0)

for i in range(1,len(A)):
  A[i] += A[i-1]
for i in range(1, len(B)):
  B[i] += B[i-1]

ans = 0
for i in range(len(A)):
  rest_time = k - A[i]
  if rest_time >= 0:
    numb = bisect_right(B, rest_time)
    anstmp = i + numb 
    ans = max(ans, anstmp)
print(ans)
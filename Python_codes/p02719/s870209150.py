N, K = map(int, input().split())
# K > 1 かつ　N > Kの場合は、N - N // K * K をスタートにできる
if K > 1:
  N = N - N // K * K
else:
  N = 0
minimum = N
count = 0
#print(N)
while count <= N / K:
  N = abs(N - K)
  minimum = min(N, minimum)
  count += 1
print(minimum)
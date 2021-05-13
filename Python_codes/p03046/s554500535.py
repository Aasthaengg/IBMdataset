M, K = map(int, input().split())
if (M == 1 and K == 1) or (K > 2**M-1):
  print(-1)
  exit()

arr = list(range(2**M))
if K == 0:
  print(' '.join(list(map(str, list(sorted(arr + arr))))))
  exit()

arr2 = arr[:K] + arr[K+1:]
print(' '.join(list(map(str, arr2 + [K] + arr2[::-1] + [K]))))
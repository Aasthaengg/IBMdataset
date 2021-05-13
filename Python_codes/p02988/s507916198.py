#ネットのやつ　自分で考える
#from math import ceil
#n, h = map(int, input().split( ))
n = int(input())
A = list(map(int, input().split( )))
ans = 0
for i in range(n-2):
  if min(A[i], A[i+2]) <= A[i+1] and A[i+1] <= max(A[i], A[i+2]):
    ans += 1
print(ans)
K = int(eval(input()))

# すべての要素に1回ずつ操作を行うことは、すべての要素を-1することと同じ。
# N=50,aiがすべてN-1である状態を最終状態として、逆算する。

N = 50
r = K % N
q = K // N
A = []
for i in range(N):
  A.append(N-1 + q + (i<r)*(N-r+1) - (i>=r)*r)
print(N)
print(*A)
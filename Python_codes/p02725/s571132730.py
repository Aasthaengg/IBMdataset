K, N = map(int, input().split())
A = list(map(int, input().split()))

L = [] #各家の間の距離

for n in range(1, N):
  L.append(A[n]-A[n-1])

L.append(A[0]+K-A[N-1]) #最初の家と最後の家の距離（起点から最初の家の距離に、最後の家から起点までの距離を足す）

ans = K - max(L)

print(ans)
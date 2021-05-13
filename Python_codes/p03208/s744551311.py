# 初期入力
import sys
input = sys.stdin.readline
N,K = (int(i) for i in input().split())
h =[0]*N
for i in range(N):
    h[i] = int(input())
h.sort()

#K本選んだうちの最高と最低の差をリスト
ans =[10**9+1]*N
for i in range(N-K+1):
    ans[i] =h[i+K-1] -h[i]
print(min(ans))
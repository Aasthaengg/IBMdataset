# AtCoder
N = int(input())
A = list(map(int, input().split()))  # ダムに溜まった水量

s = sum(A)
X = [0]*N
X[0] = s

# X1を求める
for i in range(1, N, 2):
    X[0] -= 2*A[i]

for i in range(N-1):
    X[i+1] = 2*A[i]-X[i]

print(' '.join(map(str, X)))

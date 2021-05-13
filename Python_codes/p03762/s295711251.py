n, m = map(int, input().split())
# x,yは既にソートされている
x = [0] + list(map(int, input().split()))
y = [0] + list(map(int, input().split()))

"""
図で考えるより、数式を眺めた方が見通しが良い

Σ_{1<=i<j<=n} Σ_{1<=k<l<=m} (x_j - x_i) (y_l - y_k)
（↓変数分離のような変形をする）
Σ_{1<=i<j<=n}(x_j - x_i) * Σ_{1<=k<l<=m}(y_l - y_k)

2つのΣは同じ形をしているので、左のΣの求め方を考えれば良い

n=5 で実験してみると、
x5-x4, x5-x3, x5-x2, x5-x1
x4-x3, x4-x2, x4-x1
x3-x2, x3-x1
x2-x1
+x_iは(i-1)個, -x_iは(n-i)個ある
i = 1,2,...,nについて計算すれば、O(n)で計算が可能
"""
tmp1 = 0
tmp2 = 0
for i in range(1, n + 1):
    tmp1 += (i - 1) * x[i] - (n - i) * x[i]
for j in range(1, m + 1):
    tmp2 += (j - 1) * y[j] - (m - j) * y[j]

mod = 10**9 + 7
ans = (tmp1 % mod) * (tmp2 % mod)
ans %= mod
print(ans)

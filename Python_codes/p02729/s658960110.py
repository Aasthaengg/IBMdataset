# n 偶数 m 奇数
n, m = list(map(int, input().split()))
n1=0
m1=0
# 2つ選んで偶数になる　奇数＋奇数　もしくは　偶数＋偶数

if n >= 2:
    n1 = (n * (n-1))//2

if m >= 2:
    m1 = (m * (m-1))//2

print(n1 + m1)

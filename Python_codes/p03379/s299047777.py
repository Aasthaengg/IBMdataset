import copy
n = int(input())
X = list(map(int, input().split()))
x = X.copy()
X.sort()
m_s = X[n//2 - 1]
m_l = X[n//2]
for i in x:
    if i <= m_s:
        print(m_l)
    else:
        print(m_s)
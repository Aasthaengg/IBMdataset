#081_D
n = int(input())
a = list(map(int, input().split()))
m = 0
for i in range(n):
    if abs(a[i]) > abs(m):
        m = a[i]
        m_idx = i
        
if m == 0:
    print(0)
elif m > 0:
    print(2 * n)
    for i in range(1, n+1):
        if i == 1:
            print(m_idx+1, 1)
            print(m_idx+1, 1)
        else:
            print(i-1, i)
            print(i-1, i)
else:
    print(2 * n)
    for i in range(n, 0, -1):
        if i == n:
            print(m_idx+1, n)
            print(m_idx+1, n)
        else:
            print(i+1, i)
            print(i+1, i)
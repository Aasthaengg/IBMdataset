n = int(input())
a = [0] * n; b = [0] * n
for i in range(n):
    a[i],b[i] = map(int,input().split()) 

a.sort(); b.sort()
if n%2 != 0 :
    print(b[n//2] - a[n//2] + 1)
    exit(0)

def m_r(c):
    return (c[n//2] + c[n//2 - 1])

z = m_r(b) - m_r(a) + 1
print(z)


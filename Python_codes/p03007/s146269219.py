n = int(input())
A = list(map(int,input().split()))
A.sort()
ans = []

# 全て正
if min(A)>=0:
    print(sum(A)-2*A[0])
    for i in range(n):
        if i==0:
            x = A[i]
        elif i==n-1:
            print(A[i], x)
        else:
            print(x, A[i])
            x -= A[i]

# 全て負
elif max(A)<=0:
    A = A[::-1]
    print(sum(A)*(-1)+2*A[0])
    for i in range(n):
        if i==0:
            x = A[i]
        else:
            print(x, A[i])
            x -= A[i]

# 正負
else:
    m,p = [], []
    for a in A:
        if a<0:
            m.append(a)
        else:
            p.append(a)
    print(sum(p)-sum(m))
    m.sort()
    p.sort()
    x = m[0]
    for i in range(len(p)-1):
        print(x, p[i])
        x -= p[i]
    else:
        print(p[-1], x)
        x = p[-1] - x
        
    for j in range(1, len(m)):
        print(x, m[j])
        x -= m[j]
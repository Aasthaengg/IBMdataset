n,m,X,Y = list(map(int,input().split()))
x = list(map(int,input().split()))
y = list(map(int,input().split()))

m_x = sorted(x,reverse=True)
m_y = sorted(y)

ans = "War"

for i in range(m_x[0]+1,m_y[0]+1):
    if X<i<=Y:
        ans = "No War"


print(ans)

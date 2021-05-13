n = int(input())
t = list(map(int,input().split()))
a = list(map(int,input().split()))
MOD = 10**9 + 7

m_left =[[1,t[0]]]
for i in range(1,n):
    if t[i] > t[i-1]:
        m_left.append([1,t[i]])
    else:
        m_left.append([0,t[i]])

m_right = [[1,a[n-1]]]
for i in range(n-2,-1,-1):
    if a[i] > a[i+1]:
        m_right.append([1,a[i]])
    else:
        m_right.append([0,a[i]])
m_right = m_right[::-1]
#print(m_left)
#print(m_right)

ans = 1
for i in range(n):
    if m_right[i][0] == 1 and m_left[i][0] == 1:
        if m_right[i][1] != m_left[i][1]:
            ans = 0
    elif m_right[i][0] == 1:
        if m_right[i][1] > m_left[i][1]:
            ans = 0
    elif m_left[i][0] == 1:
        if m_left[i][1] > m_right[i][1]:
            ans = 0
    else:
        ans *= min(m_right[i][1], m_left[i][1])
        ans %= MOD

print(ans)

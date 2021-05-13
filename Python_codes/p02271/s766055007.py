n = int(input())
a = list(map(int,input().split()))
q = int(input())
m = list(map(int,input().split()))

def solve(i,m):
    if m == 0:
        return True
    if i >= n:
        return False
    res = solve(i+1,m) or solve(i+1,m-a[i])
    return res

for m_tmp in m:
    if sum(a) < m_tmp:
        print('no')
    elif solve(0,m_tmp):
        print('yes')
    else:
        print('no')
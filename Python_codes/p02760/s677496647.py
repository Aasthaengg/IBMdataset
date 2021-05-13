import numpy as np
a_l = [ list(map(int, input().split())) for _ in range(3) ]
m_l = np.array([ [0]*3 for _ in range(3) ])
n = int(input())
b_l = [ int(input()) for _ in range(n) ]

def check_bingo(m_l):
    if sum(m_l[0]) == 3:
        return True
    if sum(m_l[1]) == 3:
        return True
    if sum(m_l[2]) == 3:
        return True
    if sum(m_l[:,0]) == 3:
        return True
    if sum(m_l[:,1]) == 3:
        return True
    if sum(m_l[:,2]) == 3:
        return True
    if sum([m_l[0,0],m_l[1,1],m_l[2,2]]  ) == 3:
        return True
    if sum([m_l[0,2],m_l[1,1],m_l[2,0]]  ) == 3:
        return True
    return False

for b in b_l:
    for i,a in enumerate(a_l):
        for j,v in enumerate(a):
            if b == v:
                m_l[i][j]=1
if check_bingo(m_l):
    print('Yes')
else:
    print('No')
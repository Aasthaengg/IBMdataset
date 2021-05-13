


N = int(input())

edge_num = 0
for i in range(N-1,0,-1):
    edge_num += i

edge_num -= N//2 

"""
Nが偶数の場合、1とNの間にある辺、2とN-1の間にある辺、......を外していく
Nが奇数の場合、1とN-1の間にある辺、2とN-2の間にある辺、......を外していく
"""
print(edge_num)
for i in range(1, N):
    for j in range(i+1,N+1):
        if N % 2 == 0:
            if i + j == N+1:
                continue
        else:
            if i+ j == N:
                continue
        print(i,j)
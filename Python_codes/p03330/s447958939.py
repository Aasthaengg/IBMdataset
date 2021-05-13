import collections
import itertools

def solve():
    N,C = map(int, input().split())
    transform = [list(map(int, input().split())) for _ in range(C)]
    counter = [[0]*C, [0]*C, [0]*C]
    for i in range(N):
        S = list(map(int, input().split()))
        # print(S)
        # print(S[0::3],S[1::3],S[2::3])
        for j in S[0::3]: counter[i%3][j-1] += 1
        for j in S[1::3]: counter[(i+1)%3][j-1] += 1
        for j in S[2::3]: counter[(i+2)%3][j-1] += 1 
    
    trans_0 = [sum( transform[j][i]*counter[0][j] for j in range(C) ) for i in range(C)]
    trans_1 = [sum( transform[j][i]*counter[1][j] for j in range(C) ) for i in range(C)]
    trans_2 = [sum( transform[j][i]*counter[2][j] for j in range(C) ) for i in range(C)]
    # print(counter)
    # print(trans_0,trans_1,trans_2)
    ret = min([trans_0[i]+trans_1[j]+trans_2[k] for (i,j,k) in itertools.product(range(C),repeat = 3)
               if i != j and j != k and k != i])
    # print(all_combination)
    print(ret)
    
solve()
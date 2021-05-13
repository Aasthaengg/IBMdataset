def solve():
    N = int(input())
    A = list(map(int, input().split()))
    M = 0
    ret_M = []
    memo_N = [0]*N # memo: 倍数を足したときに2で割った余り
    for i in range(N)[::-1]:
        i_ = i+1
        q = N//i_
        s = sum(memo_N[i_*(d+1)-1] for d in range(1,q))
        memo_N[i] = (s%2)^A[i]
        if memo_N[i]:
            M += 1
            ret_M.append(i_)
                
    print(M)
    if M: print(' '.join(map(str, ret_M[::-1])))
      
solve()
def solve():
    N = int(input())
    #AAwIdx = list(map(int,input().split()))
    AAwIdx = [(i,A) for i, A in enumerate(map(int, input().split()))]
    #for i in range(N):
    #    AAwIdx[i][0] = i
    #    AAwIdx[i][1] = AA[i]
    AA_sorted = sorted(AAwIdx, key=lambda x: x[1], reverse=True)
    #print(AA_sorted)

    answer = [[0]*(N+1) for _ in range(N+1)]

    ans_all = 0
    Idx_i = 0
    Idx_f = N-1
    for i in range(0,N):
        for no in range(i+1):
            idxi = i-no
            idxf = Idx_f-no
            ans = answer[i-no][no] + abs(AA_sorted[i][0]-idxi)*AA_sorted[i][1]
            if ans>answer[i+1-no][no]:
                answer[i+1-no][no] = ans
            ans = answer[i-no][no] + abs(AA_sorted[i][0]-idxf)*AA_sorted[i][1]
            if ans>answer[i-no][no+1]:
                answer[i-no][no+1] = ans
    for i in range(N,N+1):
        for no in range(i+1):
            if ans_all<answer[i-no][no]:
                ans_all = answer[i-no][no]

    print(ans_all)
solve()
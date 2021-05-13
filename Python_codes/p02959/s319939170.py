def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    tail = A[N]
    idx = N-1
    while B:
        brave = B.pop()
        if brave >= tail + A[idx]:
            ans += tail + A[idx]
            tail = 0
        else:
            ans += brave
            if brave < tail:
                tail = A[idx]
            else:
                tail = A[idx] - (brave-tail)
        idx -= 1
    print(ans)



    
if '__main__' == __name__:
    resolve()
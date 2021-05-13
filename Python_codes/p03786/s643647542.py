def main():
    import sys
    input = lambda:sys.stdin.readline().strip()
    
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()

    #累積和ac_Ai<Ai+1/2の場合を除外した数
    from itertools import accumulate
    acc_A = list(accumulate(A))

    ans = 1
    for i in range(N-2,-1,-1):
        if acc_A[i]*2<(acc_A[i+1]-acc_A[i]):
            break
        else:
            ans+=1

    print(ans)

    
if __name__=='__main__':
    main()
def main():
    import sys
    input = lambda:sys.stdin.readline().strip()
    
    N = int(input())
    A = list(map(int,input().split()))

    #大きいほうから数える
    #調和級数なので計算量はOlogN
    ans = [0]*N
    for i in range(N,0,-1):
        tmp = 0
        if N//i == 1:
            ans[i-1] = A[i-1]
        else:
            max_n = N//i
            for j in range(1,max_n):
                tmp += ans[i*(j+1)-1]
            tmp%=2

            ans[i-1] = tmp^A[i-1]

    ans_n = 0
    ans_li = []
    for i in range(N):
        if ans[i]==1:
            ans_n+=1
            ans_li.append(i+1)

    print(ans_n)
    print(*ans_li)

if __name__=='__main__':
    main()
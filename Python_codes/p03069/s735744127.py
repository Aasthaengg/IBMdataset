def main():
    #input data
    import sys
    input = lambda:sys.stdin.readline().strip()
    
    N = int(input())
    S = input()
    
    #solve
    all_black = S.count('#')
    fill_one = min(N-all_black,all_black)
    b_cnt = 0

    ans = 10**10
    for i in range(N-1):
        if S[i]=='#':
            b_cnt+=1
        else:
            pass
        tmp = b_cnt+((N-i-1)-(all_black-b_cnt))
        ans = min(tmp,ans)
        # print(i,ans)

    print(min(ans,fill_one))

if __name__=='__main__':
    main()



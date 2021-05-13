def main():
    #input data
    import sys
    input = lambda:sys.stdin.readline().strip()
    S = input()
    
    #solve
    N = len(S)
    cnt=0
    ans=0
    for i in range(N):
        if S[i]=='S':
            cnt+=1
        else:
            if cnt:
                cnt-=1
                ans+=2
    print(N-ans)


if __name__=='__main__':
    main()
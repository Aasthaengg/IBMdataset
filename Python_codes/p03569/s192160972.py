def main():
    #input data
    import sys
    input = lambda:sys.stdin.readline().strip()
    S = input()
    N = len(S)
    #solve
    left = 0
    right = N-1

    ans = 0
    while left<=right:
        if right==left:
            break
        if S[left]==S[right]:
            left+=1
            right-=1
            continue
        if S[left]!='x' and S[right]!='x':
            print(-1);exit()
        if S[left]=='x':
            left+=1
            ans+=1
        if S[right]=='x':
            right-=1
            ans+=1
    if right>left:
        print(-1)
    else:
        print(ans)


if __name__=='__main__':
    main()
n,a,b,c,d=list(map(int,input().split()))
s=input()

if c<d:
    for i in range(a-1,d-1):
        if s[i]=='#' and s[i+1]=='#':
            print('No')
            exit(0)
    print('Yes')
else:
    for i in range(b-1,d):
        if s[i-1]=='.' and s[i]=='.' and s[i+1]=='.':
            break
    else:
        print('No')
        exit(0)
    
    for i in range(a-1,c-1):
        if s[i]=='#' and s[i+1]=='#':
            print('No')
            exit(0)
    
    print('Yes')

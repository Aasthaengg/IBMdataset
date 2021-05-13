n=int(input()) 
c=list(map(int, input().split())) 
ans = 0
 
if n == 1:
    print('Yes')
    exit()
if n == 2:
    if c[0] > c[1] + 1:
        print('No')
        exit()
if n >= 3:
    for i in range(n-1):
        if c[i] > c[i+1] +1:
            print('No')
            exit()
        if c[i] == c[i+1] +1:
            ans = max(ans,c[i])
            if c[i+1] + 1 < ans:
                print('No')
                exit()


print('Yes')
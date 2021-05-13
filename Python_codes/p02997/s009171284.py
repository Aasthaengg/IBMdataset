import sys

N,K = map(int,input().split())

ans = []

for i in range(N-1):

    i += 2

    ans.append([1,i])

nsum = (N-1)*(N-2) // 2

if K == 0:
    print ( N * (N-1) //2 )
    for i in range(1,N+1,1):
        for j in range(i+1,N+1,1):
            print (i,j)
    sys.exit()

if K > nsum:
    print (-1)
    sys.exit()

for i in range(2,N+1,1):

    for j in range(i+1,N+1,1):

        if nsum == K:
            print (len(ans))
            for x,y in ans:
                print (x,y)
            sys.exit()

        ans.append([i,j])
        nsum -= 1

        
            

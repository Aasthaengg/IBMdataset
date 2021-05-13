import sys
n,k = input().split()

N = int(n)
K = int(k)

if N < K:
    print("NO")
    #sys.exit()
    
elif N == 1 and K == 1:
    print("YES")
    #sys.exit()

elif N % 2 == 0:
    if 2 * K <= N:
        print("YES")
    else:
        print("NO")

elif N % 2 == 1:
    if 2 * K <= N+1:
        print("YES")
    else:
        print("NO")
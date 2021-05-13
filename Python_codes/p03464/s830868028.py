K = int(input())
A = list(map(int,input().split()))

if A[-1] != 2:
    print(-1)
    exit()

A.reverse()
mn = mx = 2
for a,b in zip(A,A[1:]):
    mn += (b - mn%b)%b
    mx += a-1
    mx -= mx%b
    if mn > mx:
        print(-1)
        exit()

mx += A[-1]-1
print(mn,mx)
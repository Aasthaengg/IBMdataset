mod = 10**9+7
N = int(input())
A = [int(x) for x in input().split()]

def po2(x) :
    ans = 1
    for i in range(x) :
        ans = (ans*2)%mod
    return ans

if N%2 == 0 :
    B = [2*i+1 for i in range(N//2)] * 2
else :
    B = [0] + [2*(i+1) for i in range(N//2)] * 2

A.sort()
B.sort()

if A != B :
    print(0)
else :
    print(po2(N//2))

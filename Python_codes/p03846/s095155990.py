N=int(input())
A=list(map(int,input().split()))
A.sort()
if N%2==1:
    collect=list(range(0,N))[::2]*2
    collect.remove(0)
elif N % 2 == 0:
    collect = list(range(1, N))[::2] * 2

collect.sort()
if collect!=A:
    print(0)
else:
    print(2**(N//2)%(10**9+7))

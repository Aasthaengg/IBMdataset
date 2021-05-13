N=int(input())
A=sorted(list(map(int,input().split())))

MOD=10**9+7

if N%2:
    arr=sorted([0]+list(range(2,N))[::2]*2)
else:
    arr=sorted(list(range(1,N))[::2]*2)

print(2**(N//2)%MOD if A == arr else 0)
N = int(input())
P  = list(map(int, input().split()))
Q  = list(map(int, input().split()))

def func(n):
    if n==0 or n==1:
        return 1
    ans = n
    for j in reversed(range(2, n)):
        ans*=j
    return ans

def count(N, P):
    ans = 0
    a = [1]*N
    
    for i in range(N-1):
        ans+=sum(a[:P[i]-1])*func(N-1-i)
        a[P[i]-1]=0
    return ans

print(abs(count(N, Q)-count(N, P)))

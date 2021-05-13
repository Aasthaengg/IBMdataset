import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
 
N = int(input())
ans = len(make_divisors(N-1))-1
lis = make_divisors(N)
for n in lis:
    G = N
    if n==1:
        continue
    while G%n==0:
        G //= n
    if G%n==1:
        ans += 1
print(ans)
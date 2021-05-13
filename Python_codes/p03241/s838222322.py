import sys,math,collections,itertools
input = sys.stdin.readline

N,M=list(map(int,input().split()))
mn = M//N
ml = M%N
if ml == 0:
    print(mn)
    exit()
ans = 0
for i in range(mn+1,0,-1):
    if i < ans:
        break
    tmp = math.gcd(i,M-i*(N-1))
    ans = max(ans,tmp)
print(ans)

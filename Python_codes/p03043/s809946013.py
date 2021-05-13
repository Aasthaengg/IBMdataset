import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())


N,K = MI()
ans = 0
for i in range(1,N+1):
    r = 0
    while i <= K-1:
        i *= 2
        r += 1
    ans += 1/(N*2**r)

print(ans)

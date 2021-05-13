import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
a = list(map(int, input().split()))
l = max(a).bit_length()
ans = 0
M = 10**9+7
for j in range(l):
    v0 = 0
    v1 = 0    
    for i in range(n):
        if (a[i]>>j)&1:
            v1 += 1
        else:
            v0 += 1
    ans += v0*v1*pow(2,j,M)
    ans %= M
print(ans%M)
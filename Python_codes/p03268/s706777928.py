import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,k = list(map(int, input().split()))
v0 = n//k
ans = v0**3
if k%2==0:
    ans += ((n+k//2)//k) **3
print(ans)
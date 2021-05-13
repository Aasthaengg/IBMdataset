import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,a,b = list(map(int, input().split()))
if a<=b:
    if a!=b and n==1:
        ans = 0
    else:
        ans = (b*(n-1)+a) - (a*(n-1)+b) + 1
else:
    ans = 0
print(ans)
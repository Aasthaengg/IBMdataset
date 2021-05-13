import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,m = list(map(int, input().split()))
a = list(map(int, input().split()))
if n<sum(a):
    ans = -1
else:
    ans = n - sum(a)
print(ans)
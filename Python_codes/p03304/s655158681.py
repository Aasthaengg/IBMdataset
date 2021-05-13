import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,m,d = list(map(int, input().split()))
ans = 0
if d==0:
    v = n
else:
    v = 2*(n-d)
ans = (m-1)*v/pow(n,2)
print(ans)
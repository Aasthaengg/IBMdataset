import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,k = map(int, input().split())
h = list(map(int, input().split()))

h.sort()
if k>=n:
    print(0)
else:
    print(sum(h[:n-k]))
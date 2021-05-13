import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,k = map(int, input().split())
ab = [None]*n
for i in range(n):
    ab[i] = list(map(int, input().split()))
ab.sort()
for a,b in ab:
    k -= b
    if k<=0:
        print(a)
        break
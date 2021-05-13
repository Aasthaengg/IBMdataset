import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
a = [None]*n
b = [None]*n
for i in range(n):
    a[i],b[i] = map(int, input().split())
    
ab = [(a[i]+b[i], i) for i in range(n)]
ab.sort(reverse=True)
takahashi = 0
aoki = 0
for i in range(n):
    if i%2==0:
        takahashi += a[ab[i][1]]
    else:
        aoki += b[ab[i][1]]
print(takahashi-aoki)
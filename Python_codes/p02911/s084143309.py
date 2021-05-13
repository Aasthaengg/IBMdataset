import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,k,q = list(map(int, input().split()))
a = [int(input()) for _ in range(q)]
vs = [k-q]*n
for i in range(q):
    vs[a[i]-1] += 1
for i in range(n):
    if vs[i]>0:
        print("Yes")
    else:
        print("No")
import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,k = list(map(int, input().split()))
a = list(map(int, input().split()))
v = 0
v2 = 0
M = 10**9+7
for i in range(n):
    v += sum(a[i]<a[j] for j in range(i))
    v2 += sum(a[i]<a[j] for j in range(n))
#     print(v,v2)
ans = v*k
ans += v2*(k-1)*k//2
print(ans%M)
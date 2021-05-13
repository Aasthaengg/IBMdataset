import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,k = list(map(int, input().split()))
a = list(map(int, input().split()))
l = k.bit_length()
vs = [0]*(l)
for i in range(l):
    tmp = sum((item&(1<<i)) for item in a)
    if n*(1<<i) >= 2*tmp:
        vs[i] = n*(1<<i) - 2*tmp
ans = 0
tmp = 0
for i in range(l-1, -1, -1):
    if (k>>i)&1:
        ans = max(ans, tmp+sum(vs[:i]))
        tmp += vs[i]
ans = max(ans, tmp)
print(ans+sum(a))
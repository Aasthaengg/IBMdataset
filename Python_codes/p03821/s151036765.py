import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
ans = 0
a = [None]*n
b = [None]*n

for i in range(n):
    a[i],b[i] = map(int, input().split())
for aa,bb in zip(a[::-1], b[::-1]):
    aa += ans
    ans += bb*(aa//bb + (aa%bb!=0)) - aa
#     print(ans)
print(ans)
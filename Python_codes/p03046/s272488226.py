import sys
sys.setrecursionlimit(20000000)
#input = sys.stdin.readline
m,k = map(int,input().split())
if k == 0:
    ans = []
    for i in range(2**(m)):
        ans.append(i)
        ans.append(i)
    print(" ".join(map(str,ans)))
    exit()
if k > (2**(m))-1:
    print(-1)
    exit()
a = 0
for i in range(2**m):
    if i != k:
        a ^= i
if a != k:
    print(-1)
    exit()
ans = []
for i in range(2**m):
    if i == k:
        continue
    ans.append(str(i))
ans = ans + [str(k)] + ans[::-1] + [str(k)]
print(" ".join(ans))
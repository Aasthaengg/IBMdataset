import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

L, R = mapint()

lis = []
for i in range(L, min(R+1, L+2101)):
    lis.append(i)

leng = len(lis)
ans = 10**18
for i in range(leng-1):
    a = lis[i]
    for j in range(i+1, leng):
        b = lis[j]
        ans = min(ans, (a*b)%2019)
print(ans)
import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

S = list(input())
leng = len(S)
ans = 0
for i in range(1<<(leng-1)):
    lis = [S[0]]
    for j in range(leng-1):
        if (i>>j)&1:
            ans += int(''.join(lis))
            lis = []
        lis.append(S[j+1])
    else:
        if lis:
            ans += int(''.join(lis))
print(ans)
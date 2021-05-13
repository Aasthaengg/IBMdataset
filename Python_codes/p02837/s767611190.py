import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
a = [set() for _ in range(n)]
b = [set() for _ in range(n)]
for i in range(n):
    nn = int(input())
    for j in range(nn):
        x,y = list(map(int, input().split()))
        x -= 1
        if y==1:
            a[i].add(x)
        else:
            b[i].add(x)
ans = -1
for bit in range(1<<n):
    tmpa = set()
    tmpb = set()
    tmp2a = set()
    tmp2b = set()
    for j in range(n):
        if bit>>j&1:
            tmpa |= a[j]
            tmpb |= b[j]
            tmp2a.add(j)
        else:
            tmp2b.add(j)
    if len(tmpa&tmpb)==0 and len(tmp2a&tmpb)==0 and len(tmpa&tmp2b)==0: #and tmpa==tmp2:
        ans = max(ans, len(tmp2a))
print(ans)
import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
fs = [None]*n
for i in range(n):
    l = list(map(int, input().split()))
    fs[i] = set([i for i in range(10) if l[i]])
p = [None]*n
for i in range(n):
    p[i] = list(map(int, input().split()))
ans = -float("inf")
for b in range(1<<10):
    if b==0:
        continue
    score = 0
    s = set()
    for i in range(10):
        if b>>i&1:
            s.add(i)
    for i in range(n):
        score += p[i][len(s&fs[i])]
    ans = max(ans, score)
print(ans)
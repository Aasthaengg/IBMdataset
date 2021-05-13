import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
d = {(str(p),str(q)): 0 for p in range(1,10) for q in range(1,10)}
for i in range(1, n+1):
    c = str(i)
    if c[-1]!="0":
        d[c[0], c[-1]] += 1
ans = 0
for i in range(1,10):
    for j in range(1,10):
        if i==j:
            v = d[str(i), str(j)]
            ans += v * v
        else:
            v1 = d[str(i), str(j)]
            v2 = d[str(j), str(i)]
            ans += v1*v2
print(ans)
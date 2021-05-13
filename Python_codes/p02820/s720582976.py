import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,k = map(int, input().split())
r,s,p = map(int, input().split())
t = input()
ok = [False] * n
score = {"r": p, "s": r, "p": s}
ans = 0
for i in range(n):
    if i>=k and t[i-k]==t[i] and not ok[i-k]:
        ok[i] = True
    else:
        ans += score[t[i]]

print(ans)
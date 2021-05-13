import sys
input = sys.stdin.readline

X, Y, A, B, C = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
p.sort(reverse=True)
q.sort(reverse=True)
r.sort(reverse=True)
l = p[:X]+q[:Y]
l.sort()
s = sum(l)
ans = s
pre = s

for i in range(min(len(l), C)):
    ans = max(ans, pre-l[i]+r[i])
    pre = pre-l[i]+r[i]

print(ans)
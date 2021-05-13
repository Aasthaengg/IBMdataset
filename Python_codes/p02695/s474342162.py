import sys
input = lambda: sys.stdin.readline().rstrip()

N, M, Q = map(int, input().split())

l = []

for i in range(Q):
    a,b,c,d = map(int, input().split())
    l.append((a,b,c,d))

ans = 0
stack = [[1]]

while stack:
    a = stack.pop()
    if len(a) == N:
        score = 0
        for j in l:
            if a[j[1]-1] - a[j[0]-1] == j[2]:
                score += j[3]   
        ans = max(score, ans)
    else:
        for k in range(a[-1], M+1):
            s = a[:]
            s.append(k)
            stack.append(s)
print(ans) 
from collections import deque
X,Y,A,B,C = map(int,input().split())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
r = list(map(int,input().split()))
p.sort()
q.sort()
r.sort()
p = deque(p)
q = deque(q)
r = deque(r)
p.appendleft(0)
q.appendleft(0)
r.appendleft(0)


a = p.pop()
b = q.pop()
c = r.pop()
x = 0
y = 0
ans = 0
for i in range(X+Y):
    if x < X and y < Y:
        if a >= b and a >= c:
            ans += a
            x += 1
            a = p.pop()
        elif b >= c:
            ans += b
            y += 1
            b = q.pop()
        else:
            ans += c
            c = r.pop()
    elif x < X:
        if a >= c:
            ans += a
            x += 1
            a = p.pop()
        else:
            ans += c
            c = r.pop()
    else:
        if b >= c:
            ans += b
            y += 1
            b = q.pop()
        else:
            ans += c
            c = r.pop()

print(ans)

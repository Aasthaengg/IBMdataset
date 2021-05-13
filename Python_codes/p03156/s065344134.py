n = int(input())
a,b = map(int,input().split())
p = list(map(int,input().split()))

p.sort()

s = 0
t = 0

for i in p:
    if i <= a:
        s += 1
        t += 1
    elif i <= b:
        t += 1

ans = min(s, t-s, len(p)-t)

print(ans)
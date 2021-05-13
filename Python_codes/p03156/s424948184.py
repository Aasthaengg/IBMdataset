n = int(input())
a, b = map(int, input().split())
p = list(map(int, input().split()))
f, s, t = 0, 0, 0
for i in range(n):
    if p[i] <= a:
        f += 1
    elif a+1 <= p[i] <= b:
        s += 1
    else:
        t += 1
print(min(f, s, t))
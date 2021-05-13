n = int(input())
a, b = map(int, input().split())
p = list(map(int, input().split()))
p1 = []
p2 = []
p3 = []

for i in p:
    if i <= a:
        p1.append(i)
    elif a < i <= b:
        p2.append(i)
    else:
        p3.append(i)

ans = min(len(p1), len(p2), len(p3))
print(ans)
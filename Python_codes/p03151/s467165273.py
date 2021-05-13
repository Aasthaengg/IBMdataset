N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
p, s, ans = [], 0, 0
for i, (a, b) in enumerate(zip(A, B)):
    if a > b:
        p.append(a-b)
    elif a < b:
        s += b-a
        ans += 1
p.sort(reverse=1)
for x in p:
    if s > 0:
        s -= x
        ans += 1
else:
    if s > 0:
        ans = -1
print(ans)


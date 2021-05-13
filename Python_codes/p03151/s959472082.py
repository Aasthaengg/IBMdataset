n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
total = 0
ans = 0
free = []
for a, b in zip(A,B):
    if b > a:
        total += b-a
        ans += 1
    else:
        free.append(a-b)
free.sort(key=lambda x: -x)
for i in free:
    if total <= 0:
        break
    total -= i
    ans += 1
if total > 0:
    print(-1)
else:
    print(ans)


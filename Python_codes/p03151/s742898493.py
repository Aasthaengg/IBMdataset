n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

surplus = []
short = 0
cnt = 0

for i in range(n):
    if a[i] > b[i]:
        surplus.append(a[i]-b[i])
    elif b[i] > a[i]:
        short += b[i]-a[i]
        cnt += 1

surplus = sorted(surplus)
s = 0

while s < short:
    if len(surplus) == 0:
        print(-1)
        exit()

    s += surplus.pop()
    cnt += 1

print(cnt)
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

surplus = []
short = []

for i in range(n):
    if a[i] > b[i]:
        surplus.append(a[i]-b[i])
    elif b[i] > a[i]:
        short.append(b[i]-a[i])

surplus = sorted(surplus)
taken = False
cnt = 0
for i in range(len(short)):
    cost = short.pop()
    cnt += 1

    while cost > 0:
        if len(surplus) == 0:
            print(-1)
            exit()

        take = min(cost, surplus[-1])
        cost -= take
        surplus[-1] -= take

        if not taken:
            taken = True
            cnt += 1

        if surplus[-1] == 0:
            surplus.pop()
            taken = False

print(cnt)
from math import ceil


n, h = map(int, input().split())
katana = []
attacker = 0

for _ in range(n):
    array = list(map(int, input().split()))
    katana.append(array)
    if array[0] > attacker:
        attacker = array[0]

katana.sort(key=lambda x:x[1], reverse=True)

ans = 0
for i in range(n):
    if katana[i][1] < attacker:
        break
    h -= katana[i][1]
    ans += 1
    if h <= 0:
        print(ans)
        exit()

ans += ceil(h/attacker)

print(ans)
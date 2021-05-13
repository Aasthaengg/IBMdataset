A, B, C = map(int, input().split())

li = [A, B, C]

diff = max(li) * 3 - sum(li)
if diff % 2 == 0:
    print(int(diff / 2))
else:
    print(int((diff + 3) / 2))

N = int(input())

L = []
L.extend(((int(x), 3)  for x in input().split()))
L.extend(((int(x), 2)  for x in input().split()))
L.extend(((int(x), 1)  for x in input().split()))

L = sorted(L, reverse=True)

cnt_C = 0
cnt_B = 0
cnt_A = 0
for x, i in L:
    if i == 1:
        cnt_C += 1
    elif i == 2:
        cnt_B += cnt_C
    elif i == 3:
        cnt_A += cnt_B

print(cnt_A)

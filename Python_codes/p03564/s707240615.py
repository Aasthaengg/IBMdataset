n = int(input())
k = int(input())
bord = 1
for i in range(n):
    if bord * 2 <= bord + k: bord *= 2
    else: bord += k
print(bord)
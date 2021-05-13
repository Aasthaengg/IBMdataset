n = int(input())

sums = 0
answer = False
for _ in range(n):
    d1, d2 = map(int, input().split())
    if d1 == d2:
        sums += 1
    else:
        sums = 0

    if sums == 3:
        answer = True

print("Yes" if answer else "No")
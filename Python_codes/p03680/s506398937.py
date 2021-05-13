N = int(input())
al = [int(input()) for _ in range(N)]

index = 0
count = 0
for i in range(N):
    b = al[index]
    count += 1
    if b == 2:
        break
    index = b - 1

if b != 2:
    count = -1

print(count)
n = int(input())
A = list(map(int, input().split()))
kisu = 0
if n == 1:
    print("YES")
    exit()


for a in A:
    if a % 2 == 1:
        kisu += 1
if kisu % 2 == 0:
    print("YES")
else:
    print("NO")

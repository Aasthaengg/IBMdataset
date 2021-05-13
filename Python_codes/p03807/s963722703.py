n = int(input())
tp = tuple(map(int, input().split()))

even = 0
odd = 0

for i in range(n):
    if tp[i] % 2 == 0:
        even += 1
    elif tp[i] % 2 == 1:
        odd += 1

if odd % 2 == 1:
    print("NO")
else:
    print("YES")
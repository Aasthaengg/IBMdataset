N = int(input())
A = list(map(int, input().split()))

al = 1
bad = 1

for a in A:
    al *= 3
    if a % 2 == 0:
        bad *= 2

print(al - bad)

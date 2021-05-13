from collections import Counter

N = int(input())
A = list(map(int, input().split()))

colors = []
over = 0

for a in A:
    if 1 <= a <= 399:
        colors.append("gray")
    if 400 <= a <= 799:
        colors.append("brawn")
    if 800 <= a <= 1199:
        colors.append("green")
    if 1200 <= a <= 1599:
        colors.append("water")
    if 1600 <= a <= 1999:
        colors.append("blue")
    if 2000 <= a <= 2399:
        colors.append("yellow")
    if 2400 <= a <= 2799:
        colors.append("orange")
    if 2800 <= a <= 3199:
        colors.append("red")
    if 3200 <= a:
        over += 1

counter = Counter(colors)

if len(A) == over:
    print(1, over)
    exit()

if over > 0:
    max_num = len(counter) + over
    print(len(counter), max_num)
else:
    print(len(counter), len(counter))

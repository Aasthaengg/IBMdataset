N = int(input())
H = list(map(int, input().split()))

before = H[0]

for h in H:
    if before > h:
        print("No")
        break
    if before < h:
        before = h - 1
    if before == h:
        before = h
else:
    print("Yes")

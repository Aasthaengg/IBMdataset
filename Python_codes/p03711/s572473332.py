a1 = (1, 3, 5, 7, 8, 10, 12)
a2 = (4, 6, 9, 11)
a, b = map(int, input().split())
if a == 2 or b == 2:
    print("No")
    exit()
f = 1
if a in a1 and b in a1:
    f = 0
if a in a2 and b in a2:
    f = 0
print("YNeos"[f::2])
ans = []

def paint(h, w):
    a = []
    for i in range(h):
        if i == 0 or i == h - 1:
            a.append("#" * w)
        else:
            a.append("#" + "." * (w - 2) + "#")
    ans.append("\n".join(a))

while True:
    H, W = map(int, input().split())
    if H == W == 0: break

    paint(H, W)

print(("\n" * 2).join(ans), "\n", sep = "")

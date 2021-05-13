ans = []

def paint(h, w):
    a = []
    for i in range(h):
        a.append("")
        for j in range(w):
            a[-1] += ["#", "."][(i + j) % 2]
    ans.append("\n".join(a))

while True:
    H, W = map(int, input().split())
    if H == W == 0: break

    paint(H, W)

print(("\n" * 2).join(ans), "\n", sep = "")

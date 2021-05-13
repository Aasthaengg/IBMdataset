
def resolve():
    nnn = int(input())
    for h in range(1, 3501):
        for w in range(1, 3501):
            div = 4 * h * w - nnn * h - nnn * w
            if div == 0:
                continue
            n = nnn * h * w / div
            if int(n) == n and 0 < n:
                print(h, w, int(n))
                return

if __name__ == "__main__":
    resolve()

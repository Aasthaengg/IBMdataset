class PrintAFrame:
    def output(self, H, W):
        s1 = ""
        s2 = ""
        for w in range(W):
            s1 += "#"
            if w == 0 or w == W - 1:
                s2 += "#"
            else:
                s2 += "."
        for h in range(H):
            if h == 0 or h == H - 1:
                print s1
            else:
                print s2
        print

if __name__ == "__main__":
    pf = PrintAFrame()
    while True:
        h, w = map(int, raw_input().split())
        if h == 0 and w == 0:
            break
        pf.output(h, w)
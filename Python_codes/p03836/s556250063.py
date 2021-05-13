def main():
    sx, sy, tx, ty = map(int, input().split())

    dy = ty - sy
    dx = tx - sx

    cmd = ""
    cmd += ("U"*dy + "R"*dx)
    cmd += ("D"*dy + "L"*dx)
    cmd += ("L" + "U"*(dy+1) + "R"*(dx+1) + "D")
    cmd += ("R" + "D"*(dy+1) + "L"*(dx+1) + "U")

    print(cmd)

if __name__ == "__main__":
    main()
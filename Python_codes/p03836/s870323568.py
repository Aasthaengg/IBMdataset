def main():
    sx, sy, tx, ty = map(int, input().split())
    x = tx - sx
    y = ty - sy
    s = ""
    for i in range(2):
        tmp = ""
        if i:
            tmp += "D"
            tmp += "R"*(x+1)
            tmp += "U"*(y+1)
            tmp += "L"

        else:
            tmp += "R"*x
            tmp += "U"*y
        s += tmp + tmp.translate(str.maketrans({"U": "D",
                                                "D": "U", "L": "R", "R": "L"}))
    print(s)


if __name__ == "__main__":
    main()

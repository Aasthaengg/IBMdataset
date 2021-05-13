def main():
    sx, sy, tx, ty = map(int, input().split())
    x = tx - sx
    y = ty - sy
    s = ""
    s += "R"*x
    s += "U"*y
    s += s.translate(str.maketrans({"U": "D",
                                    "D": "U", "L": "R", "R": "L"}))
    tmp = ""
    tmp += "D"
    tmp += "R"*(x+1)
    tmp += "U"*(y+1)
    tmp += "L"
    s += tmp + tmp.translate(str.maketrans({"U": "D",
                                            "D": "U", "L": "R", "R": "L"}))
    print(s)


if __name__ == "__main__":
    main()

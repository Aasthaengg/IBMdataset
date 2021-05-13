# vim: fileencoding=utf-8


def main():

    n = int(input())
    li = []
    for i in range(n):
        x, y, h = map(int, input().split())
        li.append({"x": x, "y": y, "h": h})
    li.sort(key=lambda x: x["h"], reverse=True)

    tops = []
    for i in range(101):
        for j in range(101):
            h = li[0]["h"] + abs(li[0]["x"] - i) + abs(li[0]["y"] - j)
            tops.append({"x": i, "y": j, "h": h})

    for i in range(1, n):
        tmp = []
        for j in range(len(tops)):
            x = li[i]["x"]
            y = li[i]["y"]
            h = li[i]["h"]
            topX = tops[j]["x"]
            topY = tops[j]["y"]
            topH = tops[j]["h"]
            if h == max(topH - abs(topX - x) - abs(topY - y), 0):
                tmp.append(tops[j])
        tops = tmp
    print(f"{tops[0]['x']} {tops[0]['y']} {tops[0]['h']}")


if __name__ == "__main__":
    main()

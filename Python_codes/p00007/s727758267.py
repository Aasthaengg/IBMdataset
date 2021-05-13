# 累積計算

if __name__ == "__main__":
    n = int(input())
    # print(n)

    y = 100000  # 10万　100,000
    y2 = y / 1000
    for i in range(0, n):

        y4 = y2 * 1.05
        # y3 = round(y2 * 1.05 -0.5, 0)
        y3 = float(int(y2 * 1.05))
        #print("  {} {}".format(y4, y3))
        if y4 - y3 > 0:
            y4 += 1
        y2 = int(y4)
        #print("{} {}".format(i, y2 * 1000))

    print(y2 * 1000)

    # 0 105,000
    # 1 110,250 -> 111,000
    # 2 116,550 -> 117,000
    # 3 122,850 -> 123,000
    #4 129,150 -> 130,000
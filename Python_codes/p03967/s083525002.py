def resolve():
    s = input()
    win, lose = 0, 0
    hands = {0: "g", 1: "p"}
    for i in range(len(s)):
        h = hands[i % 2]
        if s[i] == "g" and h == "p":
            win += 1
        elif s[i] == "p" and h == "g":
            lose += 1
    print(win - lose)


if __name__ == "__main__":
    resolve()

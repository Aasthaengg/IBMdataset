def main():
    words = int(input())
    first_b = [""]
    last_a = [""]
    others = []
    ab = []
    for _ in range(words):
        s = input()
        if s[0] == "B" and s[-1] == "A":
            ab.append(s)
        elif s[-1] == "A":
            last_a.append(s)
        elif s[0] == "B":
            first_b.append(s)
        else:
            others.append(s)
    connect = []
    for i in range(max(len(last_a), len(first_b))):
        if i < len(last_a) - 1:
            connect.append(last_a[i])
        if i < len(first_b) - 1:
            connect.append(first_b[i])
    word = last_a[-1] + "".join(ab) + first_b[-1] + "".join(connect) + "".join(others)
    print(word.count("AB"))


if __name__ == '__main__':
    main()


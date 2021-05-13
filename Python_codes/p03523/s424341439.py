def main():
    s = input()
    l = ["K", "I", "H", "B", "R"]
    for i in range(len(l)):
        if l[i] not in s:
            print("NO")
            exit()

    c = 0
    ac = 0
    for i in range(len(s)):
        if c == 0:
            if s[i] == "K":
                c = 1
                ac = 0
            elif s[i] != "A":
                print("NO")
                exit()
            else:
                ac += 1
            if ac > 1:
                print("NO")
                exit()
        elif c == 1:
            if s[i] != "I":
                print("NO")
                exit()
            c = 2
        elif c == 2:
            if s[i] != "H":
                print("NO")
                exit()
            c = 3
        elif c == 3:
            if s[i] == "B":
                c = 4
                ac = 0
            elif s[i] != "A":
                print("NO")
                exit()
            else:
                ac += 1
            if ac > 1:
                print("NO")
                exit()
        elif c == 4:
            if s[i] == "R":
                c = 5
                ac = 0
            elif s[i] != "A":
                print("NO")
                exit()
            else:
                ac += 1
            if ac > 1:
                print("NO")
                exit()
        elif c == 5:
            if s[i] == "A":
                ac += 1
            else:
                print("NO")
                exit()
            if ac > 1:
                print("NO")
                exit()
    print("YES")


if __name__ == '__main__':
    main()
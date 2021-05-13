def main():
    flag = True
    while flag:
        s1, tr, s2 = input().split()
        s1, s2 = int(s1), int(s2)
        if tr == "+":
            print(s1 + s2)
        elif tr == "-":
            print(s1 - s2)
        elif tr == "*":
            print(s1 * s2)
        elif tr == "/":
            print(s1 // s2)
        else:
            flag = False
            break


if __name__=="__main__":
    main()
def main():
    s = input()
    l = "abcdefghijiklmopqrstuvwxyz"

    for i in range(len(s)):
        l = l.replace(s[i], '')

    if l == "":
        print('None')
    else:
        print(l[0])


if __name__ == "__main__":
    main()

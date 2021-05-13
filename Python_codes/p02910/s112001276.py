def main():
    s = input()
    odds = ("R", "U", "D")
    even = ("L", "U", "D")
    ans = True
    for index, i in enumerate(s, 1):
        if index % 2 == 0 and not i in even:
            ans = False
        if index % 2 != 0 and not i in odds:
            ans = False

    print("Yes" if ans == True else "No")


main()
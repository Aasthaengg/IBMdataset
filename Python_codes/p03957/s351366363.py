def main():
    word = input()
    index = [word.find("C"), 0]
    if index[0] >= 0:
        index[1] = word.find("F", index[0])
    print("Yes" if index[0] >= 0 and index[1] >= 0 else "No")


if __name__ == '__main__':
    main()


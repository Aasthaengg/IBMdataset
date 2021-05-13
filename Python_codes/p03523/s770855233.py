def main():
    S = input()
    ans_can = {"AKIHABARA", "KIHABARA", "AKIHBARA", "AKIHABRA", "AKIHABAR",
               "KIHABAR", "AKIHABR", "AKIHBAR", "AKIHBRA", "KIHABRA", "KIHBR",
               "AKIHBR", "KIHABR", "KIHBAR", "KIHBRA", "KIHBARA"}
    if S in ans_can:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()

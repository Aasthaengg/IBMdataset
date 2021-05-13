def main():
    s = input()
    lst = ["AKIHABARA",
           "KIHABARA", "AKIHBARA", "AKIHABRA", "AKIHABAR",
           "KIHBARA", "KIHABRA", "KIHABAR", "AKIHBRA", "AKIHBAR", "AKIHABR",
           "KIHBRA", "KIHBAR", "KIHABR", "AKIHBR",
           "KIHBR"]

    if s in lst:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()

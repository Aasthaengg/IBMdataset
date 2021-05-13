def main():
    S = input()
    ans = {"AKIHABARA", "KIHABARA", "AKIHBARA", "AKIHABRA", "AKIHABAR",
           "KIHBARA", "AKIHABR", "KIHABAR", "KIHBRA", "AKIHBR",
           "KIHABR", "KIHBAR", "KIHABRA", "AKIHBAR", "AKIHABAR", "KIHBR"}
    print("YES" if S in ans else "NO")


if __name__ == '__main__':
    main()

import sys

input = sys.stdin.readline


def main():
    S = input().rstrip()

    # AKIHABARA
    correct_list = [
        "AKIHABARA",
        "KIHABARA",
        "AKIHBARA",
        "AKIHABRA",
        "AKIHABAR",
        "KIHBARA",
        "KIHABRA",
        "KIHABAR",
        "AKIHBRA",
        "AKIHBAR",
        "AKIHABR",
        "KIHBRA",
        "KIHBAR",
        "KIHABR",
        "AKIHBR",
        "KIHBR",
    ]

    is_correct = False
    for correct in correct_list:
        if S == correct:
            is_correct = True
            break

    if is_correct:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()

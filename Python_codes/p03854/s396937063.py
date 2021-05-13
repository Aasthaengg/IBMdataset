import re


def main():
    print("YES" if re.match("^(dream|dreamer|erase|eraser)+$", input()) else "NO")


if __name__ == "__main__":
    main()

import re


def main(s: str):
    if re.fullmatch(r"A?KIHA?BA?RA?", s):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    s = input()

    main(s)

import re


def resolve():
    s = input()
    print("Yes" if re.match(r".*C.*F.*", s) else "No")


if __name__ == "__main__":
    resolve()

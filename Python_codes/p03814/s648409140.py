import sys
def input(): return sys.stdin.readline().strip()


def main():
    s = input()
    l = len(s)
    forward = 0
    while s[forward] != "A": forward += 1
    back = -1
    while s[back] != 'Z': back -= 1
    print(l - forward + back + 1)

if __name__ == "__main__":
    main()

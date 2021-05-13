import sys
def input(): return sys.stdin.readline().strip()


def main():
    N = input()
    nine = False
    for c in N:
        if c == '9': nine = True
    if nine:
        print("Yes")
    else:
        print("No")



if __name__ == "__main__":
    main()

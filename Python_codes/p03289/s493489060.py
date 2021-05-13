# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()

def resolve():
    import sys
    input = sys.stdin.readline
    s = input().rstrip()

    has_c = False

    for i, c in enumerate(s):
        if i == 0:
            if c != "A":
                print("WA")
                return
            continue
        if i in list(range(2, len(s) - 1)) and c == "C":
            if has_c:
                print("WA")
                return
            has_c = True
        else:
            if not c.islower():
                print("WA")
                return

    if not has_c:
        print("WA")
        return
    print("AC")

if __name__ == "__main__":
    resolve()

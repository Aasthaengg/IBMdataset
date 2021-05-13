
def resolve():
    import sys
    import string
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    # n = int(input().rstrip())
    s = input().rstrip()
    alphabets = set()
    for c in string.ascii_lowercase:
        alphabets.add(c)

    for c in s:
        if c in alphabets:
            alphabets.remove(c)
            if len(alphabets) == 0:
                print("None")
                return

    print(sorted(alphabets)[0])

if __name__ == "__main__":
    resolve()

# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()

def resolve():
    import sys
    input = sys.stdin.readline
    s = input().rstrip()
    t = input().rstrip()

    for i in range(100):
        rotated = s[i:] + s[:i]
        if rotated == t:
            print("Yes")
            return

    print("No")

if __name__ == "__main__":
    resolve()

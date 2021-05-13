
def resolve():
    import sys
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    # n = int(input().rstrip())
    # s = input().rstrip()

    h, w = [int(x) for x in input().rstrip().split(" ")]

    print("".join(["#" for _ in range(w+2)]))

    for i in range(h):
        print("#"+input().rstrip()+"#")

    print("".join(["#" for _ in range(w+2)]))

if __name__ == "__main__":
    resolve()

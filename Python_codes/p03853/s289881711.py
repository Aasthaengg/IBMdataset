# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()

def resolve():
    import sys
    input = sys.stdin.readline
    h, w = [int(x) for x in input().rstrip().split(" ")]
    for i in range(h):
        c = input().rstrip()
        print(c)
        print(c)

if __name__ == "__main__":
    resolve()

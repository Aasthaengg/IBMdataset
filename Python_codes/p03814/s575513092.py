# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()

def resolve():
    import sys
    input = sys.stdin.readline

    s = input().rstrip()

    print(s.rfind("Z") - s.find("A") + 1)

if __name__ == "__main__":
    resolve()

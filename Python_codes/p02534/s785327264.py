
def resolve():
    import sys

    input = sys.stdin.readline

    n = int(input().rstrip())
    print("".join("ACL" for _ in range(n)))
    



if __name__ == "__main__":
    resolve()

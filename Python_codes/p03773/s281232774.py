import sys
def input(): return sys.stdin.readline().strip()

def main():
    a, b = map(int, input().split())
    val = a + b
    if val >= 24: val -= 24
    print(val)


if __name__ == "__main__":
    main()

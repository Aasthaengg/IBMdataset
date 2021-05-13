import sys
def input(): return sys.stdin.readline().strip()

def main():
    a, b, c = map(int, input().split())
    possible = False
    for i in range(b):
        if a * i % b == c:
            possible = True
            break
    if possible:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()

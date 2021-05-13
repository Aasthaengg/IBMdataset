import sys
def input(): return sys.stdin.readline().strip()

def main():
    h, w = map(int, input().split())
    C = [input() for _ in range(h)]
    for c in C:
        print(c)
        print(c)



if __name__ == "__main__":
    main()

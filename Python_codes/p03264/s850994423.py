import sys
def input(): return sys.stdin.readline().strip()


def main():
    k = int(input())
    if k % 2 == 0: print((k // 2) ** 2)
    if k % 2 != 0: print(((k - 1) // 2) * (k + 1) // 2)
    

if __name__ == "__main__":
    main()

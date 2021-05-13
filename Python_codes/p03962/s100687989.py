import sys
def input(): return sys.stdin.readline().strip()

def main():
    a, b, c = map(int, input().split())
    ans = {a, b, c}
    print(len(ans))






if __name__ == "__main__":
    main()

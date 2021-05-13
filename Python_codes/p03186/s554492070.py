import sys
input = sys.stdin.readline

def main():
    A, B, C = map(int, input().split())
    poison = min(A+B, C)
    if poison < C:
        poison += 1
    print(poison + B)

if __name__ == "__main__":
    main()

import sys
input = sys.stdin.readline

def main():
    A, B, C = input().strip().split()

    if A[-1] == B[0] and B[-1] == C[0]:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
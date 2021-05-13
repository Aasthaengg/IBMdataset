import sys
input = sys.stdin.readline


def main():
    A,B = [int(i) for i in input().strip().split()]

    if A % 3 == 0 or B % 3 == 0 or (A + B) % 3 == 0:
        print("Possible")
    else:
        print("Impossible")

if __name__ == "__main__":
    main()
import sys
input = sys.stdin.readline

def main():
    X = int(input())
    for A in range(-118, 120):
        for B in range(-118, 120):
            if A ** 5 - B ** 5 == X:
                print(A, B)
                sys.exit()

main()
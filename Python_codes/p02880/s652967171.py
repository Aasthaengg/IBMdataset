import sys
input = sys.stdin.readline

def main():
    N = int(input())
    # N = 10
    ok = False
    for i in range(1, 10):
        for j in range(1, 10):
            if i*j == N:
                ok = True
                break
        if ok:
            break
    print("Yes" if ok else "No")


if __name__ == "__main__":
    main()
import sys
input = sys.stdin.readline

def main():
    N = int(input())
    for i in range(1, 10):
        if N%i == 0:
            t=N//i
            if 0 < t and t < 10:
                print("Yes")
                return
    print("No")
    return

if __name__ == "__main__":
    main()

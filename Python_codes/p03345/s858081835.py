# coding: utf-8

def main():
    A, B, _, K = map(int, input().split())
    ans = A - B if K % 2 == 0 else B - A
    print(ans)

if __name__ == "__main__":
    main()

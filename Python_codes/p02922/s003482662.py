# -*- coding: utf-8 -*-

def main():

    A, B = map(int, input().split())

    ans = 0

    while True:
        num = (A - 1) * ans + 1
        if num >= B:
            break
        
        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
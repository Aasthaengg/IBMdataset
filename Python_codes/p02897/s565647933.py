# -*- coding: utf-8 -*-

def main():

    N = int(input())

    num = 0

    for i in range(N + 1):
        if i % 2 > 0:
            num += 1
    
    ans = num / N

    print(ans)


if __name__ == "__main__":
    main()
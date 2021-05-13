# -*- coding: utf-8 -*-

def main():

    W, a, b = map(int, input().split())

    if a + W < b:
        ans = b - (a + W)

    elif b + W < a:
        ans = a - (b + W)
    
    else:
        ans = 0

    print(ans)


if __name__ == "__main__":
    main()
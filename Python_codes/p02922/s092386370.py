# coding: utf-8

def main():
    a, b = map(int, input().split())
    quo = (b - 1) // (a - 1)
    rem = (b - 1) % (a - 1)
    if rem == 0:
        print(quo)
    else:
        print(quo+1)

if __name__ == "__main__":
    main()
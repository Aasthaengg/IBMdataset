import math

def main():
    a, b = [int(x) for x in input().split()]

    if(a < b):
        print(0)
    else:
        print(10)


if __name__ == "__main__":
    main()
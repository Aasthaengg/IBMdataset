from itertools import combinations as comb


def main():
    a, b, c = map(int, input().split())
    if a == (b+c) or b == (a+c) or c == (a+b):
        ans = 'Yes'
    else:
        ans = "No"
    print(ans)


if __name__ == "__main__":
    main()

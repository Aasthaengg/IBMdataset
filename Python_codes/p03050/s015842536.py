from math import sqrt
def main():
    n = int(input())
    ans = 0
    for i in range(1, int(sqrt(n))+1):
        y = n - i
        if y % i == 0 and y != 0 and n//(y//i) == i:
            ans += y // i
    print(ans)

if __name__ == "__main__":
    main()
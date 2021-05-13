import math

def main():
    N = int(input())
    ans = N
    for i in range(1, int(math.sqrt(N)) + 1):
        if N % i != 0:
            continue
        j = N // i
        d = (i - 1) + (j - 1)
        if d < ans:
            ans = d
    print(ans)


if __name__ == '__main__':
    main()

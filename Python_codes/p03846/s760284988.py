from collections import Counter
def main():
    n = int(input())
    A = list(map(int, input().split()))
    c = Counter(A)
    mod = 1000000007
    if n % 2 == 0:
        if any([a % 2 == 0 for a in A]) or any([v != 2 for v in c.values()]):
            print(0)
            exit()

    else:
        if any([a % 2 != 0 for a in A]) or any([v != 2 if k != 0 else v != 1 for k, v in c.items()]):
            print(0)
            exit()
    print(pow(2, n // 2, mod))    


if __name__ == '__main__':
    main()

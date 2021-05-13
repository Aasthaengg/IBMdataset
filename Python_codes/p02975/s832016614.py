from collections import Counter
def main():
    n = int(input())
    A = list(map(int, input().split()))
    c = Counter(A)
    if c[0] == n:
        print('Yes')
    elif n % 3 == 0 and c[0] == n // 3 and len(set(A)) == 2:
        print('Yes')
    elif n % 3 == 0 and len(set(A)) == 3:
        x, y, z = list(set(A))
        if x ^ y ^ z == 0 and c[x] == c[y] == c[z]:
            print('Yes')
        else:
            print('No')
    else:
        print('No')


if __name__ == '__main__':
    main()

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    A.sort()
    from collections import Counter
    c = Counter(A)
    if 0 in c.keys() and c[0] == N:
        return print("Yes")
    elif N % 3 == 0 and 0 in c.keys() and c[0] == N//3 and\
            len(c.keys()) == 2:
        return print("Yes")
    elif N % 3 == 0 and len(c.keys()) == 3 and \
            all(N//3 == v for v in c.values()):
        ans = 0
        for k in c.keys():
            ans ^= k
        if ans != 0:
            return print("No")
        else:
            return print("Yes")
    else:
        return print("No")


if __name__ == '__main__':
    main()

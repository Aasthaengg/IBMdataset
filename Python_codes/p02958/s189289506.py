def main():
    n = int(input())
    p = [int(i) for i in input().split()]
    for i in range(n):
        for j in range(i, n):
            p[i], p[j] = p[j], p[i]
            if is_sorted(p):
                print("YES")
                return
            p[i], p[j] = p[j], p[i]
    print("NO")


def is_sorted(p):
    for i in range(len(p) - 1):
        if p[i] > p[i + 1]:
            return False
    return True


if __name__ == '__main__':
    main()

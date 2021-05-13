def main():
    import sys
    N = int(input())
    left = 0
    right = N
    table = ["?"]*N
    print(left)
    sys.stdin.flush()
    le = input()
    if le == "Vacant":
        return
    table[left] = le

    for i in range(20):
        c = (left + right) // 2
        print(c)
        sys.stdin.flush()
        s = input()
        if s == "Vacant":
            return
        table[c] = s
        if (c - left) % 2 == 0 and table[left] == table[c]:
            left = c
        elif (c - left) % 2 == 1 and table[left] != table[c]:
            left = c
        else:
            right = c


if __name__ == '__main__':
    main()

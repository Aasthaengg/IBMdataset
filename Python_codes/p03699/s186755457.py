
def main():
    n = int(input())
    s = []
    for _ in range(n):
        ss = int(input())
        s.append(ss)

    total = sum(s)
    if total % 10 != 0:
        print(total)
        return
    s.sort()

    for i, ss in enumerate(s):
        if ss % 10 != 0:
            print(total-ss)
            return
    print(0)

if __name__ == '__main__':
    main()

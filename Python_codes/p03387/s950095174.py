import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    a, b, c = map(int, input().split())
    r = 0
    if a % 2 == b % 2 == c % 2:
        pass
    else:
        # 奇数が１つ → 偶数に+1
        if (a + b + c) % 2 == 1:
            a += 1 if a % 2 == 0 else 0
            b += 1 if b % 2 == 0 else 0
            c += 1 if c % 2 == 0 else 0
        # 奇数が２つ → 奇数に+1
        else:
            a += 1 if a % 2 == 1 else 0
            b += 1 if b % 2 == 1 else 0
            c += 1 if c % 2 == 1 else 0
        r += 1
    r += ((max(a, b, c) * 3 - (a + b + c)) // 2)
    print(r)

if __name__ == '__main__':
    main()
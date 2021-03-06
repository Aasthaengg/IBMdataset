# Vol0005.
import sys


def intinput():
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    return a

def get_gcd(x, y):
    if x < y: return get_gcd(y, x)
    # x >= yのときはx % yを計算してyとx % yの話にする。
    # ここでx % yのところが0ならばyが求める答えとなる。
    if y == 0: return x
    return get_gcd(y, x % y)

def main():
    data = []
    lines = sys.stdin.readlines()

    for line in lines:
        data.append(line.split())

    N = len(data)
    for i in range(N):
        a = int(data[i][0]); b = int(data[i][1])
        gcd = get_gcd(a, b)
        lcm = (a // gcd) * b
        print('%d %d' % (gcd, lcm))

if __name__ == "__main__":
    main()

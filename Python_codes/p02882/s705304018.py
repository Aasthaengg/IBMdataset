def main():
    import sys
    readline = sys.stdin.buffer.readline

    import math

    a, b, x = map(int, readline().split())

    c = a*a*b
    if x <= a*a*b/2:
        ans = math.atan2(a*b*b, 2*x)
    else:
        ans = math.atan2(2*(a*a*b-x), a**3)
    print(math.degrees(ans))

if __name__ == '__main__':
    main()
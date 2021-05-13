import sys
import math
input = lambda: sys.stdin.readline().rstrip()

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

def main():
    a, b, c, d = map(int, input().split())
    a_cnt, b_cnt = 0, 0
    a -= 1
    a_cnt = a - ((a//c + a//d) - a // lcm(c, d))
    b_cnt = b - ((b//c + b//d) - b // lcm(c, d))
    print(b_cnt - a_cnt)
    
if __name__ == '__main__':
    main()
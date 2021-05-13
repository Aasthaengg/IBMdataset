from decimal import Decimal
import sys
input = sys.stdin.readline

def main():
    A, B = map(Decimal, input().split())
    ans = int(A * B)
    print(ans)

main()
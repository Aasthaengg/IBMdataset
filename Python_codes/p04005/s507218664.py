#!/usr/bin/env python3

def main():
    A, B, C = map(int, open(0).read().split())

    m = A*B*C
    ans = min(abs(2*A*C*(B//2) - m), abs(2*C*B*(A//2) - m), abs(2*B*A*(C//2) - m))

    print(ans)


main()
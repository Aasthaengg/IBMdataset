import sys
input = sys.stdin.readline

n, k = [int(x) for x in input().split()]

print(k * (k - 1)**(n - 1))
import sys
readline = sys.stdin.buffer.readline

n,k = map(int,readline().split())

print(k * (k-1)**(n-1))
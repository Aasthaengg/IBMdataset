import sys
input = sys.stdin.readline
n = int(input())
d_li = [int(w) for w in input().split()]
d_li.sort()

print(d_li[n // 2] - d_li[n // 2 - 1])

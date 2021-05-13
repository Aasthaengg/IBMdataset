import sys
input = sys.stdin.readline
N = int(input())
a = [int(i) for i in input().split()]
a.sort()
print(a[-1] - a[0])
import sys
n = int(input())
a_ls = [int(i) for i in sys.stdin.readline().split()]
a_ls = [i - j - 1 for j, i in enumerate(a_ls)]
base = sorted(a_ls)[n // 2]
print(sum([abs(a - base) for a in a_ls]))
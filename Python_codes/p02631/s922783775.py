import sys
n = int(input())
a_ls = [int(i) for i in sys.stdin.readline().split()]
ans = 0
for a in a_ls:
    ans ^= a
print(" ".join([str(ans ^ a) for a in a_ls]))
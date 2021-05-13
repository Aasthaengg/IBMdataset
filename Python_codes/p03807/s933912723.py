import sys
n = int(input())
a_ls = [int(i) for i in sys.stdin.readline().split()]
if sum([i % 2 for i in a_ls]) % 2 == 0:
    print("YES")
else:
    print("NO")
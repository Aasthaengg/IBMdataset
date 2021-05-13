import sys
n = int(input())
a_ls = []
for i in range(n):
    a = int(sys.stdin.readline().strip())
    a_ls.append(a)
if all([a % 2 == 0 for a in a_ls]):
    print("second")
else:
    print("first")
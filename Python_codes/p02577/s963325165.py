import sys

input = sys.stdin.readline

n = input()
n = n.replace('\n','')

n_list = list(n)


su = 0
for n in n_list:
    n_int = int(n)
    su += n_int

if su % 9 == 0:
    print("Yes")
else:
    print("No")
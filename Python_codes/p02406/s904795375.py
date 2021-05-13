def check_num(n):
    if n % 3 == 0\
    or n % 10 == 3\
    or str(n).find("3") != -1:
        print(" {0}".format(n), end="")

n = int(input())
for i in range(3, n+1):
    check_num(i)
print()
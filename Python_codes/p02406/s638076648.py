n = int(input())
for N in range(3, n+1):
    if N % 3 == 0\
    or N % 10 == 3\
    or str(N).find("3") != -1:
        print(" {0}".format(N), end = "")
print()
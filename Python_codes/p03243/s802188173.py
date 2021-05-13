import sys
N = int(sys.stdin.readline().rstrip())
for i in range(N, 10**5):
    if len(set(list(str(i)))) == 1:
        print(i)
        exit()
# ABC081
N = int(input())
A = list(map(int, input().split()))

i = 1
while True:
    for a in A:
        if a % (2**i) == 0:
            pass
        else:
            print(i-1)
            exit()
    i += 1

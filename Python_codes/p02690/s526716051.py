import sys
X = int(input())

for A in range(-119, 121, 1):
    for B in range(-119, 121, 1):
        if A**5 - B**5 == X:
            print("{} {}".format(A, B))
            sys.exit()

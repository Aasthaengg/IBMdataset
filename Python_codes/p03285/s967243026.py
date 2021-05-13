import sys
N = int(input())
for i in range(0,26):
    for j in range(0,16):
        if N == 4*i +7*j:
            print("Yes")
            sys.exit()
print("No")
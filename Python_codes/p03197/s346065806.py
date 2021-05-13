import sys
def input():
    return sys.stdin.readline()[:-1]
N=int(input())
a=[int(input())for i in range(N)]
for i in a:
    if i%2:
        print("first")
        break
else:
    print("second")
import sys
input = sys.stdin.readline
X = int(input())
A = int(input())
B= int(input())
X -= A
tmp = X
while True:
    tmp -= B
    if tmp < 0:
        print(X)
        break
    X = tmp
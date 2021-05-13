import sys
input = sys.stdin.readline
N = int(input())
if N == 1 :
    print("Hello World")
else :
    sum = 0
    for i in range(2) :
        a = int(input())
        sum+=a
    print(sum)
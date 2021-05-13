import sys
input = sys.stdin.readline
A,P= [int(i) for i in input().split()]
sum = 3 * A + P
k = sum//2
print(k)
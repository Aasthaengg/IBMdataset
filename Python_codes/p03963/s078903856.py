import sys

n, k = map(int, input().split())

pattern = k * ((k-1)**(n-1))

print("{}".format(pattern))
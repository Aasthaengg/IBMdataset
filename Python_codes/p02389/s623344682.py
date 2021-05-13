import sys

lst = sys.stdin.read().split(" ")

a = int(lst[0])
b = int(lst[1])

print str(a*b) + " " + str(2*(a+b))
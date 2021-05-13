import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

a, b = instrm()

c = a+b

for i in range(1000):
    if i**2 == int(c):
        print("Yes")
        exit()

print("No")

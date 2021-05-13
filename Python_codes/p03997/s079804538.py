import sys
readline = sys.stdin.buffer.readline

a = int(readline())
b = int(readline())
n = int(readline())

print(((a+b)*n)//2)
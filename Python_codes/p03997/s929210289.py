import sys

def main(a,b,h):
    return (a+b)*h//2

a =int(sys.stdin.readline().strip())
b =int(sys.stdin.readline().strip())
h =int(sys.stdin.readline().strip())

print(main(a,b,h))

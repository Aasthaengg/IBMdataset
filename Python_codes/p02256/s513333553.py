import sys


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
    
if __name__ == '__main__':
    ab = sys.stdin.readline()
    a, b = ab.split()
    a, b = int(a), int(b)
    
    sys.stdout.write(str(gcd(a, b)) + '\n')
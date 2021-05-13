import sys

def get_input():
    return map(int, input().split(' '))

def gcd(i,j):
    if i > j:
        if i % j == 0:
            return j
        else:
            return gcd(j, i % j)
    else:
        if j % i == 0:
            return i
        else:
            return gcd(i, j % i)
    
def main():
    for line in sys.stdin:
        ls = list(map(int, line.split(' ')))
        g = gcd(ls[0], ls[1])
        print(g, int(ls[0]*ls[1]/g))

if __name__ == '__main__':
    main()
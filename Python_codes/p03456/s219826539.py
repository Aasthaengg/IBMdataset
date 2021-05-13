import math

def main():
    a, b = map(int, input().split())
    n = str(a) + str(b)
    N = int(n)
    if math.sqrt(N) % 1 == 0:
        print('Yes')
    else:
        print('No')
main()
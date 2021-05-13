import numpy as np
def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    print(np.gcd.reduce(a))
main()
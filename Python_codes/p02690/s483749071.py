import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
import numpy as np
def main():
    x = int(input())
    for i1 in range(-201, 201):
        for i2 in range(-201, 201):
            if i1**5 - i2**5 == x:
                print(i1, i2)
                sys.exit()

if __name__ == '__main__':
    main()
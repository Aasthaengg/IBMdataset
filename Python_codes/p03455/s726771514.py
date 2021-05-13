from sys import stdin
readline = stdin.buffer.readline
read = stdin.buffer.read
def i_input(): return int(input().rstrip())
def i_map(): return map(int, input().rstrip().split())
def i_list(): return list(i_map())

# import numpy as np
# from numba import jit
# stdin = open('sample.txt')

def main():
    A, B = i_map()
    if (A * B) % 2 == 0:
        print('Even')
    else:
        print('Odd')

if __name__ == "__main__":
    main()

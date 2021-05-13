#!/usr/bin/python

def main():
    A, B = [int(x) for x in input().split()]
    if divisor(A, B) == True:
        print(A + B)
    else:
        print(B - A)

def divisor(A, B):
    if B % A == 0: return True 
    return False


if __name__ == "__main__":
    main()
from sys import stdin

def main():
    A, B = [int(x) for x in stdin.readline().rstrip().split()]
    if A > 2*B:
        print(A - 2*B)
    else:
        print(0)
main()
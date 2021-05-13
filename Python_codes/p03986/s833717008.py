
import sys
sys.setrecursionlimit(10 ** 8)

def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    X = input()
    s = False
    c = cc = 0
    for i in range(len(X)):
        if X[i] == 'S':
            s = True
            cc += 1
        else:
            s = False
            if cc > 0:
                cc -= 1
                c += 1
    print(len(X)-2*c)

    return

if __name__ == '__main__':
    main()

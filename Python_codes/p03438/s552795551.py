import sys
sys.setrecursionlimit(10 ** 8)

def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    N = Z()
    A = ZZ()
    B = ZZ()
    if A == B:
        print('Yes')
        return
    sa, sb = sum(A), sum(B)
    if sa >= sb:
        print('No')
        return

    numDo = sb - sa
    x = y = 0
    for a, b in zip(A, B):
        if a > b: x += (a - b)
        elif a < b: y += (b-a+1)//2
    print('Yes' if x <= numDo and y <= numDo else 'No')

    return

if __name__ == '__main__':
    main()

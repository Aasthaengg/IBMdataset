import sys
import collections
input = sys.stdin.readline

def main():
    N, T = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]

    maxlist = [0] * N
    ma = 0
    for i in range(N - 1, -1, -1):
        ma = max(ma, A[i])
        maxlist[i] = ma

    c = collections.Counter()

    for i in range(N - 1):
        c[maxlist[i + 1] - A[i]] += 1

    m = sorted(c.keys(), reverse=True)


    print(c[m[0]])



    
    
    

if __name__ == '__main__':
    main()



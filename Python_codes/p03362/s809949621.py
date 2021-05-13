import sys
def input():
    return sys.stdin.readline()[:-1]
def main():
    N = int(input())
    P = []
    for k in range(2,2000):
        f = 1
        for i in range(2,int(k**(1/2))+2):
            if k%i == 0:
                f = 0
                break
        if f == 1 and k%5 == 1:
            P.append(k)
    print(*P[:N])
if __name__ == '__main__':
    main()

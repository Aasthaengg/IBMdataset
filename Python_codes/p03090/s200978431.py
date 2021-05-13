import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    NI = lambda : int(sys.stdin.readline())

    N = NI()
    ans = []
    for i in range(1,N):
        for j in range(i+1,N+1):
            if not j == (N - i + (N%2==0)):
                ans.append((i,j))
    print(len(ans))
    for x in ans:
        print(x[0],x[1])


if __name__ == '__main__':
    main()
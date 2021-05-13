import sys
input = sys.stdin.readline

def sol():
    N,M = list(map(int,input().split()))
    A = list(map(int,input().split()))
    tmp = sorted([list(map(int,input().split())) for _ in range(M)],key = lambda x:-x[1])
    cnt = 0
    t = []
    for a,b in tmp:
        t+=[b]*a
        cnt = cnt + a
        if cnt >=N:
            break

    A += t
    A.sort(reverse = 1)
    print(sum(A[:N]))

if __name__ == '__main__':
    sol()

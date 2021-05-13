MOD = 10 **9 + 7
INF = 10 ** 10

def main():
    K = int(input())
    A = list(map(int,input().split()))
    m = 2
    M = 2
    flag = True
    for i in range(K - 1,-1,-1):
        x = (m + A[i] - 1)//A[i]
        y = M//A[i]
        if x > y:
            flag = False
            break
        M = y*A[i] + A[i] - 1
        m = x*A[i]
    if flag:
        print(m,M)
    else:
        print(-1)         
if __name__ == '__main__':
    main()
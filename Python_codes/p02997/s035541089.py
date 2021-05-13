import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
def main():
    n, k = list(map(int, input().split()))
    a = (n-1)*(n-2)//2
    if k > a:
        print('-1')

    else:
        print(n-1+a-k)
        #頂点1を中心とするスターグラフ作成
        for i in range(2, 1+n):
            print(1, i)

        cnt = 0
        for i in range(2, n):
            for j in range(i+1, n+1):
                if cnt >= a-k:
                    return
                print(i, j)
                cnt += 1

main()


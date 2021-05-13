def main():
    k, n = map(int, input().split())
    A = [int(x) for x in input().split()]
    # AnからA0までを取り除いたものを初期値にする
    minv = A[n-1] - A[0]
    #️ A0からA1の距離...An-1からAnの距離をkから引いた値を比較してちいさいものが答え
    for i in range(n-1):
        minv = min(minv, k - (A[i+1] - A[i]))
    print(minv)

if __name__ == '__main__':
    main()
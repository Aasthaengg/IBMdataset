#atcoder template
def main():
    import sys
    imput = sys.stdin.readline
    #文字列入力の時は上記はerrorとなる。
    #ここにコード
    #input
    n, m = map(int, input().split())

    #output
    #先頭が犬の場合
    #犬同士の隙間はn-1通りある。
    #ここのすべてに猿が入らないといけない
    #したがって、m = n-1でないといけない。
    #犬の並び方はn!通り
    #猿の並び方はm!通り

    #先頭が猿の場合
    #n = m-1でないといけない。
    mod = pow(10, 9) + 7
    dog = 1
    monkey = 1

    for i in range(1, n+1):
        dog *= i
        dog %= mod
    for j in range(1, m+1):
        monkey *= j
        monkey %= mod

    answer = 0
    # %%
    if m - n == 1:
        answer = dog * monkey % mod
    elif n- m == 1:
        answer = dog * monkey % mod
    elif n - m == 0:
        answer = dog * monkey * 2 % mod

    # %%
    print(answer)

    #N = 1のときなどcorner caseを確認！
if __name__ == "__main__":
    main()
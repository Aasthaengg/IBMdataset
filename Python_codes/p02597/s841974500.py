#atcoder template
def main():
    import sys
    imput = sys.stdin.readline
    #文字列入力の時は上記はerrorとなる。
    #ここにコード
    #input
    n = int(input())
    c = str(input())

    #output
    #Rがr個、Wがw個あるとする。
    #最終的にはRRRR...WWWW...の状態にすれば良い。
    #もとの状態と比べた時、RとWが一致していないものを考える。
    #WRの個数とRWの個数をそれぞれx, yとすると、求める操作の回数はmax(x, y)となる。
    w, r = 0, 0
    for i in range(n):
        if c[i] == "W":
            w += 1
        else:
            r += 1
    x, y = 0, 0
    for j in range(r):
        if c[j] == "W":
            x += 1
    for k in range(r+1, r+w):
        if c[k] == "R":
            y += 1
    print(max(x, y))

    #N = 1のときなどcorner caseを確認！
if __name__ == "__main__":
    main()
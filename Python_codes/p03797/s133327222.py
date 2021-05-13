
def main():
    n,m = map(int,input().split())
    s = n
    c = m
    scc = 0

    #sを全部使い切る
    take = min(s,c//2) #Sの個数とcを2で割った個数。小さい方を選んでSを使い切る
    scc += take
    s -= take
    c -= take * 2

    #残ったCでsccを作る（s=cが2個　cc=cが2個　合計4個必要）
    take = c // 4
    scc += take

    print(scc)


if __name__ == '__main__':
    main()

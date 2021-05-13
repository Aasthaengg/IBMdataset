
def main():
        
    N,C = map(int, input().split())

    #　各時間各チャンネルで録画機が動いてるかどうか
    R = [[0]*(10**5) for _ in range(C)]

    for _ in range(N):
        s,t,c = map(int, input().split())
        #チャンネルｃをｓからｔまで録画、ｓの0.5秒前から録画機を使うのでs-1始まりにする
        R[c-1][s-1:t] = [1] * (t-(s-1))

    ans = 0
    for t in range(10**5):
        cnt = 0
        #時刻ごとにそれぞれのチャンネルで録画機を使ってるかどうか数え上げる
        for ch in range(C):
            if R[ch][t] == 1: cnt += 1

        ans = max(ans, cnt)

    print(ans)

if __name__ == "__main__":
    main()
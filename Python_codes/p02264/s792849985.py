# ALDS1_3_B.
# ラウンドロビンスケジューリング。

def main():
    data = input().split()
    n = int(data[0]); q = int(data[1])
    list = [] # ここに順に格納していく感じ。
    for i in range(n):
        list.append(input().split())
        list[i][1] = int(list[i][1])
    t = 0
    while len(list) > 0:
        if list[0][1] > q:
            name = list[0][0]; time = list[0][1]
            del list[0]
            list.append([name, time - q])
            t += q
        else:
            t += list[0][1]
            print(list[0][0] + " " + str(t))
            del list[0]

if __name__ == "__main__":
    main()


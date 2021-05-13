cand_num, tenka = map(int, input().split(" "))
candles = list(map(int, input().split(" ")))
mini = 10 ** 9

for i in range(cand_num - tenka + 1):
    if candles[i] * candles[tenka + i - 1] >= 0:
        temp = max(abs(candles[i]), abs(candles[tenka + i - 1]))
    else:
        temp = min(abs(candles[i]), abs(candles[tenka + i- 1])) * 2 + max(abs(candles[i]), abs(candles[tenka + i - 1]))
    mini = temp if mini > temp else mini
print(mini)
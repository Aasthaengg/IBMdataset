N = int(input())
series = list(map(int,input().split()))


series_sorted = series[:]
series_sorted.sort()

def make_no_decrease(condition, series):
    if condition == 0:#正の整数列
        for i in range(1,N):
            print(i, i+1)
    elif condition == 1:#負の整数列
        for i in range(1,N):
            print(N-i+1, N-i)
            
if series_sorted[0]  >= 0: #正の時
    print(len(series)-1)
    make_no_decrease(0, series)
elif series_sorted[-1] < 0: #負の時
    print(len(series)-1)
    make_no_decrease(1, series)
else:
    if abs(series_sorted[-1]) <= abs(series_sorted[0]): #負の値のほうが大きい時
        print(2*len(series)-1)
        min = series.index(series_sorted[0])
        for i in range(len(series)):
            print(min+1, i+1)
        make_no_decrease(1, series)
    elif abs(series_sorted[0]) < abs(series_sorted[-1]): #正の値のほうが大きい時
        print(2*len(series)-1)
        max = series.index(series_sorted[-1])
        for i in range(len(series)):
            print(max+1, i+1)
        make_no_decrease(0, series)
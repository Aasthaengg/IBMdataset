def main():
    n = int(input()) # 2 >= n
    min_value = int(input())
    max_profit = - 10 ** 9
    for i in range(n-1):
        now_value = int(input())
        tmp_profit = now_value - min_value

        if now_value < min_value:
            min_value = now_value
        if max_profit < tmp_profit:
            max_profit = tmp_profit

        #print(i+1,now_value,max_profit)
    print(max_profit)
    return


main()

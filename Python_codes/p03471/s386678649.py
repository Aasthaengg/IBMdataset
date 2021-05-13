num, money = map(int, input().split())
ex = False

#一万円の枚数
l = 0
count_list = [-1]*3
if num*1000 <= money and money <= num*10000:
    while ex == False and l <= num:
        for i in range((num-l) + 1):
            #iを5000円の枚数
            money_actual = l*10000 + i*5000 + (num-l-i)*1000
            # print(str(money_actual))
            if money_actual == money:
                ex = True
                count_list = [l, i, num-(l+i)]
                # print(count_list)
        l += 1
        

print(str(count_list[0]) + " " + str(count_list[1]) + " " + str(count_list[2]))
def main():
    N = int(input())

    tmp = 0
    lst1 = [] #合計としては伸びるけど途中にマイナスがあるもの
    lst1_append = lst1.append

    lst2 = [] #合計してもマイナス　途中もマイナス
    lst2_append = lst2.append

    minas = 0

    for _ in range(N):
        S = list(input())
        min_ = 0
        total = 0
        for s in S:
            if s == '(':
                total += 1
            else:
                total -= 1
                min_ = min(min_, total)
        if min_ == 0:
            tmp += total
        else:
            if total > 0:
                lst1_append([min_, total])
            elif total == min_:
                minas += total
            else:
                lst2_append([min_, total])

    lst1.sort(key = lambda x: x[0], reverse = True) #途中での小さくなり方が小さいものから入れる どんどん条件は緩くなるから小さくなる値が0に近いものから
    for a, b in lst1:
        if tmp + a < 0:
            print ('No')
            exit()
        else:
            tmp += b

    lst2.sort(key = lambda x: x[1], reverse = True)
    lst2.sort(key = lambda x: x[0], reverse = False) #どんどん条件が厳しくなるから、より小さいもの　= 0から遠いもの　から使っていく

    # print (lst2)
    for a, b in lst2:
        if tmp + a < 0:
            print ('No')
            exit()
        else:
            tmp += b
    
    tmp += minas

    if tmp == 0:
        print ('Yes')
    else:
        print ('No')

if __name__ == '__main__':
    main()

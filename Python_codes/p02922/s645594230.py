a, b = map(int, input().split())
# a：電源タップ1個あたりの口数
# b：増やしたいタップ口数

def calc(a, b):
    ans_list = [a]
    add_tap = a
    
    # タップを増やさなくてもよい場合を考慮
    if b == 1:
        print(0)
    else:      
        for i in range(19):
            add_tap += a-1
            ans_list.append(add_tap)

        for i, value in enumerate(ans_list):
            if value >= b:
                print(i+1)
                break
            
calc(a, b)
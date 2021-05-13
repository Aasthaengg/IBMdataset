NUM = 20005

table = [""]*NUM

while True:
    T = str(input())
    if T == '-':
        break

    left = 0
    right = 0
    #長い配列にパターン文字列を転記
    for i in range(len(T)):
        #print(T[right])
        table[left+right] = T[right]
        right += 1

    num_shuffle = int(input())

    for loop in range(num_shuffle):
        pick_num = int(input())
        #先頭からpick_num文字を末尾に転記し、論理削除
        for i in range(pick_num):
            table[right+i] = table[left+i]
        left += pick_num
        right += pick_num

    for i in range(left,right):
        print("%s"%(table[i]),end = "")
    print()

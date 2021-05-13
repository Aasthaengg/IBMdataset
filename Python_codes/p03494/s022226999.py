
n = int(input())
a_list = list(map(int, input().split()))

ans = 0

_break = False

while _break == False:
    
    for i in range(n):

        # print("i : {0}".format(i))

        # 対象が偶数
        if a_list[i] % 2 == 0 :

            a_list[i] = a_list[i] / 2

            # 最後まで回りきったら+1
            if i == n - 1 :
                ans += 1
        # 対象が奇数　→ 終了
        else :
            _break = True
            break

print(ans)
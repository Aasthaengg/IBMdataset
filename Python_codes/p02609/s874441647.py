import collections
n = int(input())
x = input()

num_of_one = x.count("1")

#xの中に1が1つもない時
if num_of_one == 0:
    for i in range(n):
        print(1)
#xの中に1が1つの時(1を取り除くと0個になる)
elif num_of_one == 1:
    for i in range(n):
        if x[i] == "1":
            print(0)
        else:
            #1が2個なので偶数なら余り0
            if x[-1] == "0" and i != n-1:
                print(1)
            #奇数なら1回1を経由
            else:
                print(2)
else:
    dic = collections.defaultdict(int)
    #0からnまでの回数を予め求めて辞書に格納
    for i in range(n):
        tmp_p = i

        cnt = 0
        while tmp_p:
            tmp_p %= bin(tmp_p).count("1")
            cnt += 1
        dic[i] = cnt


    #2冪を num_of_one ± 1 で割った余りの配列を用意しておく
    bi_mod_p = [1 % (num_of_one+1)]
    bi_mod_m = [1 % (num_of_one-1)]
    for i in range(1,n):
        bi_mod_p.append((bi_mod_p[-1] * 2) % (num_of_one+1))
        bi_mod_m.append((bi_mod_m[-1] * 2) % (num_of_one-1))

    #xと逆順なので合わせる
    bi_mod_p.reverse()
    bi_mod_m.reverse()

    #xの10進表記を num_of_one ± 1 で割った余りを用意する
    sum_p = 0
    sum_m = 0
    for i in range(n):
        if x[i] == "1":
            sum_p += bi_mod_p[i]
            sum_p %= (num_of_one+1)
            sum_m += bi_mod_m[i]
            sum_m %= (num_of_one-1)
    tmp = 0
    for i in range(n):
        # 0 -> 1 の変化。1が増えるのでpの方を使う
        if x[i] == "0":
            tmp = sum_p + bi_mod_p[i]
            tmp %= (num_of_one+1)

        # 1 -> 0 の変化。1が減るのでmの方を使う
        else:
            tmp = sum_m - bi_mod_m[i]
            if tmp < 0:
                tmp += (num_of_one-1)
            tmp %= (num_of_one-1)
        print(dic[tmp]+1)

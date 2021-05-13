n = int(input())
x = input()

count = x.count("1")

mod1 = 0 # 1少ない
mod2 = 0 # 1多い

#　初回の各桁のbitを反転させた場合のmod結果を格納するリスト
mod1_list = [0]*n
mod2_list = [0]*n

now1 = 1

x = x[::-1]

# mod1の計算
for i in range(n):
    mod1_list[i] = now1
    if x[i] == "1":
        mod1 += now1%(count+1)
    now1 *= 2
    now1 %= (count+1)

mod1 %= (count+1)

now2 = 1

# mod2の計算
if count >= 3:
    for i in range(n):
        mod2_list[i] = now2
        if x[i] == "1":
            mod2 += now2%(count-1)
        now2 *= 2
        now2 %= (count-1)
    
    mod2 %= (count-1)

mod1_list = mod1_list[::-1]
mod2_list = mod2_list[::-1]
x = x[::-1]

for i in range(n):
    total = 1
    if x[i] == "1":
        if count == 1:
            print(0)
            continue
        elif count == 2:
            print(1)
            continue
        now = mod2-mod2_list[i]
        now %= (count-1)
    else:
        now = mod1+mod1_list[i]
        now %= (count+1)

    while now != 0:
        now = now%(bin(now).count("1"))
        total += 1

    print(total)
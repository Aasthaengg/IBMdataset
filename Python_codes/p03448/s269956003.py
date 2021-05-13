
a = int(input())
b = int(input())
c = int(input())
x = int(input())

ans = 0

for i in range(a + 1):
    # 500円玉の枚数を1枚ずつ増やす

    if x < (i * 500) :
        break

    for j in range(b + 1):
        # 100円玉の枚数を1枚ずつ増やす

        if x < ((i * 500) + (j * 100)):
            break

        for k in range(c + 1):
            # 50円玉の枚数を1枚ずつ増やす

            # print("500円玉 : {0} 枚".format(i))
            # print("100円玉 : {0} 枚".format(j))
            # print("50円玉  : {0} 枚".format(k))

            if x < (i * 500) + (j * 100) + (k * 50):
                break

            if (i * 500) + (j * 100) + (k * 50) == x :
                ans += 1
                # print('OK')

print(ans)

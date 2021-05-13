N = int(input())
S = input()

ans = 0

# find()は最初に一致した部分のみを返す
# 3桁の番号なので高々1000通り調べれば良いだけ
# N<=30000、N(C)3通り全部調べようとすると10**12個くらい調べることになって死ぬ

# 1桁目
for x in range(10):
    if S.find(str(x)) >= 0:
        temp1 = S[S.find(str(x)) + 1:]

        # 2桁目
        for y in range(10):
            if temp1.find(str(y)) >= 0:
                temp2 = temp1[temp1.find(str(y)) + 1:]

                # 3桁目
                for z in range(10):
                    if temp2.find(str(z)) >= 0:
                        ans += 1

print(ans)
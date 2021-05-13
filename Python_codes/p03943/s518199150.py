x = input()
ls_x = x.split()

# 文字配列を整数化
# for i in range(len(ls_x)):
#     ls_x[i] = int(ls_x[i])

# 別の方法　lint_xという箱を作って，intしたものをappendしていく
lint_x = []
for i in ls_x:
    lint_x.append(int(i))

lint_x = sorted(lint_x)

if (lint_x[0] + lint_x[1] == lint_x[2]):
    print("Yes")
else:
    print("No")

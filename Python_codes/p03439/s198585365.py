# https://atcoder.jp/contests/apc001/tasks/apc001_c
# nが奇数かつ同性がとなりに座ることはないので、男女は交互である。
# 制限回数が20回のところから、おそらくLogで求められる。
n = int(input())

# 0番についてクエリを投げ、結果を受け取る
q = 0
print(q)
zero = input()

if zero == "Vacant":
    exit()

left = 1
right = n - 1


for _ in range(19):
    q = (left + right) // 2
    print(q)
    s = input()
    if s == "Vacant":
        exit()
    elif q % 2 == 0:
        if s == zero:
            left = q + 1
        else:
            right = q
    else:
        if s == zero:
            right = q
        else:
            left = q + 1


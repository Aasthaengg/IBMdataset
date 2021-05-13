a, b, c, k = map(int, input().split())

flg = 0
if a - b > 0 and k % 2 == 0 or a-b < 0 and k % 2 == 0:
    flg = 1
elif a - b < 0 and k % 2 == 1 or a-b > 0 and k % 2 == 1:
    flg = -1

if abs(a-b) > 10 ** 18:
    print("Unfair")
else:
    print((a-b)*flg)
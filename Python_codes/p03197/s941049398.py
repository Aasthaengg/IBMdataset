n = int(input())
a = [int(input()) for _ in range(n)]
# print(n)
# print(a)

# - 色iのりんごの個数 ai
# - 1つ以上取る
# - 最後を取ったら勝ち

flag = all(a[i] % 2 == 0 for i in range(n))
if flag:
    print("second")
else:
    print("first")
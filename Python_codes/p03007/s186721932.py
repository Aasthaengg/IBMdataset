# 正整数だけ存在する場合はどうなるだろうか
# absじゃないのが味噌で、最後のyは負数だとお得
# なのでそれまでにできるだけ負の方向にデカいyを作ってみる
# 1 2 4 4 5 8 みたいなとき 1を出発点として残りは全部引いていけるので、最後ではy=1-(2+4+4+5)=-14にできる んで最後に最大値から引くことで 8-(-14)が達成可能
# 負数だけの場合
# 上記を踏まえると唯一の負数は正数で育てることができるが、複数ある場合はどうなるだろうか
# -6 -4 -3 -1 -1 みたいなとき
# 一度でも正数が作れればいいので-1-(-6-4-3-1)=13か？

# -1 1 2 のとき
# 最小値だけで正数を達成することはできない なので最後の手番までにできるだけデカい負を作って最後に引くをする
# -4 -2 -1 3 4 のとき 負数で正を作ると-1-(-2-4)=5, [3 4 5]になってしまいなんか小さくなりそう
# 負数を育てると-4-3-4=-11, -1-(-11)=10, 10-(-2)=12ができそうで、こっちのほうがいい
# 正の数が最後の1つになるまで負を太らせ、あとは負たちを正から引くことであますことなくいただける

n = int(input())
a = sorted(list(map(int, input().split())))
if n == 2:
    print(a[1] - a[0])
    print(a[1], a[0])
    exit()
ans = []
tmp = 0
if a[0] >= 0:
    tmp = a[0]
    for i in range(1, n - 1):
        ans.append(f"{tmp} {a[i]}")
        tmp -= a[i]
    ans.append(f"{a[-1]} {tmp}")
    tmp = a[-1] - tmp
elif a[-1] <= 0:
    tmp = a[-1]
    for i in range(n - 2, -1, -1):
        ans.append(f"{tmp} {a[i]}")
        tmp -= a[i]
else:
    ok, ng = 0, n
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if a[mid] < 0:
            ok = mid
        else:
            ng = mid
    plus = a[ok + 1:]
    minus = a[:ok + 1]
    tmp = minus[0]
    idx = 0
    while idx < len(plus) - 1:
        ans.append(f"{tmp} {plus[idx]}")
        tmp -= plus[idx]
        idx += 1
    ans.append(f"{plus[idx]} {tmp}")
    tmp = plus[idx] - tmp
    for i in range(1, len(minus)):
        ans.append(f"{tmp} {minus[i]}")
        tmp -= minus[i]

print(tmp)
for av in ans:
    print(av)

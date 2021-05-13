n = int(input())
a = list(map(int,input().split()))
#逆数を足すようの変数を用意して
v = 0.0
for i in a:
    #あとは逆数足していって
    v += 1.0 / i
#最後に逆数取るだけ
print(1.0 / v)

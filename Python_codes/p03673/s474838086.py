n = int(input())
a = list(map(int,input().split()))
o = []
#とりあえず後ろから1つ飛ばしで並べる。
for i in range(n)[::-2]:
    o.append(a[i])
#前からも1つ飛ばしで並べる。
#被らないように、要素数が奇数の時は、0番目ではなく1番目から並べる
for i in range(n)[n%2::2]:
    o.append(a[i])
print(*o)

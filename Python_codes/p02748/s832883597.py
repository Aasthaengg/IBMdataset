A, B, M = map(int, input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

#割引を使わなくても一番安い価格を初期値にする
total = min(a) + min(b)

for i in range(0,M,1):
    c = list(map(int,input().split()))  #割引券を入手
    kakaku = a[c[0]-1]+ b[c[1]-1] - c[2]
    if total > kakaku:
        total = kakaku

print(total)

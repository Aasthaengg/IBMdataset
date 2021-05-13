a = [int(s) for s in input().split()]
N = a[0]
si = a[1]
ti = a[2]
s = [int(input()) for i in range(N)]
s = sorted(s)
X = int(0)
ans = int(0)

#全員乗るまで繰り返す
while N != X:
    #まずバスを用意して先頭を乗せる
    X += 1 
    ans += 1
    #この時点で全員乗ったら終わりにする
    if N == X:
        break
    #バスの残りsi-1枠に乗れるだけ乗せる
    #そもそも乗客がsi-1人もいない場合は残りのN-X人が上限
    temp = X
    for i in range(min([si-1,N-X])):
        if s[temp + i] <= s[temp-1] + ti:
            X += 1
        else:
            break

print(ans)
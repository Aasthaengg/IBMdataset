n, m = map(int,input().split())

#sがあればcを可能な限り使う

if n == 0: #sが無かったら
    ans = m//4 #c4個につき1個作れる

elif m == 0: #cが無かったら
    ans = 0 #1個も作れない

elif n*2 <= m: #cを全部使ってもcが余るもしくはぴったりの場合
    ans = n + (m-2*n)//4 #sを使い切り、余ったcで何個か作る

elif n*2 > m: #Sが余る場合
    ans = m//2

print(ans)
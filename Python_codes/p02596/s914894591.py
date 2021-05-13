k = int(input())

t = 7
t %= k

for i in range(k+1):
    if t == 0:
        print(i+1)
        break
    #常に余りを用いる　⇒　10**7桁の演算
    t = (t*10 + 7)%k
else:print(-1)

"""
else:
for(while)文を
break文で抜ける（真）　⇒　実行しない
forのイテラブルを使い切る、whileが偽になる　⇒　実行する
"""
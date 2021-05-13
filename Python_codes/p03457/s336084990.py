#Coding by Rute
#ABC086 C - Travelingの解説を始めます。この問題ですが条件分岐によりO(N)で解くことが出来ました。
N = int(input())
now_t = 0 #現在のtとします。
now_x = 0 #現在のxとします。
now_y = 0 #現在のyとします。
flag = 0 #フラグ関数です。flag = 1のときNo, 0のときYesを出力します。
for i in range(N):
    t,x,y = map(int,input().split())
    #条件判定としては、|x-now_x|+|y-now_y| ≦ |t-now_t| かつ |x-now_x|+|y-now_y|の偶奇が|t-now-t|と一致するかどうかを判断すれば良いです。
    #なお、after contestがないケースは、|x-now_x|+|y-now_y| ≦ t で全て通っていました。
    if abs(x-now_x)+abs(y-now_y)<= abs(t-now_t) and (abs(x-now_x)+abs(y-now_y))%2 == abs(t-now_t)%2:
        now_t = t
        now_x = x
        now_y = y
    else:
        flag += 1
        break
if flag == 0:
    print("Yes")
else:
    print("No")

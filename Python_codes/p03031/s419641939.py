n,m = map(int,input().split())
q = [list(map(int, input().split())) for i in range(m)]
p= list(map(int, input().split()))
ans = 0
 
for s in range(2**n): #スイッチのon/offの状態の総当たり（2**n通り）
    judge = True
    for i in range(m): #電球1つずつに対して
        cnt=0
        for j in range(1,len(q[i])): #sの総当たりでqに当てはまるものを探す。kはforを1からにすれば無視できる。
            w=q[i][j]
            if s >> (w-1) &1 ==1: #sをw-1回シフトさせて(w-1)個目のスイッチがonか判定
                cnt+=1 #onになっているスイッチの個数をカウント
        if cnt % 2 != p[i]: #スイッチの個数を2で割った余りがpiに等しいか判定
            judge = False
    if judge:
        ans += 1
 
print(ans)
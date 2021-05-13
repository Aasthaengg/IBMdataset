


N,M = map(int, input().split())
xyz = [tuple(map(int, input().split())) for _ in range(N)]

"""
x,y,zのそれぞれの和の合計を最大化するなら、x+y+zの大きいほうから選べばいい
だが、今回はそれぞれの和の絶対値の合計を最大化。

なので、x,y,zについて、それぞれを正で絶対値を大きくするか、負で絶対値を大きくするかの戦略がある
なんというか、たとえばxを負で、y,zを正で積むとき、それぞれのxの最終結果への寄与度が-xになる。
なので、x,y,zをそのままか-1倍して和をとって、その合計でソートして決めるとよい気がする（自信があるわけではないが）

"""

ans = 0
for bit in range(1 << 3):
    
    total = 0
    coef = [1,1,1]
    for i in range(3):
        if not (bit & (1 << i)):
            coef[i] *= -1

    
    arr = []
    for i in range(N):
        arr.append((coef[0]*xyz[i][0] + coef[1]*xyz[i][1] + coef[2]*xyz[i][2], xyz[i][0], xyz[i][1], xyz[i][2]))
    arr.sort(reverse=True)
    tmp_x = tmp_y = tmp_z = 0
    for i in range(M):
        tmp_x += arr[i][1]
        tmp_y += arr[i][2]
        tmp_z += arr[i][3]
    
    ans = max(ans, abs(tmp_x) + abs(tmp_y) + abs(tmp_z))


print(ans)

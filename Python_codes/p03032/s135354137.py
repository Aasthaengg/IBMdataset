import copy

N, K = map(int, input().split())
V = [int(i) for i in input().split()]

result = 0
# i個取る
for i in range(min(N,K)+1):
    #print('i:',i)
    for sp in range(i+1): # 左右の分け方
        #print('right',sp)
        #print('left',i-sp)
        tmp = []
        V_tmp = copy.copy(V)
        #print('元々：',V_tmp)
        tmp.extend(V_tmp[:sp]) # 左端追加
        #print('left',V_tmp[:sp])
        tmp.extend(V_tmp[N-(i-sp):]) #右端追加
        #print('right',V_tmp[N-(i-sp):])
        #print(tmp)
        tmp = sorted(tmp)
        value = sum(tmp)
        # ret個戻す
        for ret in range(0, min(K-i,i)): #残り操作回数か取った石の個数iの小さい方
            if ret < i:
                # マイナスの価値は戻す
                if tmp[ret] < 0:
                    value -= tmp[ret]
                    #print('捨てた宝石：',tmp[ret])
            else:
                break
        result = max(result,value)
            #print()

print(result)

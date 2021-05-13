import math
n = int(input())
T = [0]*n
A = [0]*n
Tvote = [0]*n
Avote = [0]*n

for i in range(n):
    T[i], A[i] = map(int,input().split())

for k in range(n):
    if k == 0:
        Tvote[k] = T[k]
        Avote[k] = A[k]
    else:
        '''
        j = math.ceil(max(Tvote[k-1]/T[k],Avote[k-1]/A[k]))
        print(Tvote[k-1]/T[k])
        print(Avote[k-1]/A[k])
        print(max(Tvote[k-1]/T[k],Avote[k-1]/A[k]))
        print(j)
        print(Avote[k-1], A[k]*j)
        print(bool(Avote[k-1]<A[k]*j))
        print(bool(j>Avote[k-1]/A[k]))
        '''
        j = int(min(Tvote[k-1]//(-T[k]),Avote[k-1]//(-A[k])))*-1
        #普通に割り算やると誤差で死ぬ（floatがむずい。）
        # // は整数の除算で常に負の無限大方向に丸められる
        #一度も float になることがないはずなので、正しい計算結果が出る
        #https://paiza.hatenablog.com/entry/2017/08/01/Python3%E3%81%A7%E5%B7%A8%E5%A4%A7%E3%81%AA%E6%B5%AE%E5%8B%95%E5%B0%8F%E6%95%B0%E8%A8%88%E7%AE%97%E3%81%AE%E7%B5%90%E6%9E%9C%E3%81%8C%E5%A4%89%E3%81%A0%E3%81%A3%E3%81%9F%E3%81%AE%E3%81%A7%E7%90%86
        #正の無限大方向に丸めたいので-1かけてから計算して（丸めて）あとで-1かける。その際Av/AとTv/Tの比較も逆をとるのに注意
#        j = 1
#        while Tvote[k-1]>j*T[k] or Avote[k-1]>j*A[k]:
#            j += 1
#これは投票数が多すぎるのでTLE
        Tvote[k] = j*T[k]
        Avote[k] = j*A[k]
#    print("---input:{}:{}--vote{}:{}--diff{}".format(T[k],A[k],Tvote[k],Avote[k],bool(T[k]/A[k]==Tvote[k]/Avote[k])))   

#print("---Tvote:{}".format(Tvote))
#print("---Avote:{}".format(Avote))
#print('hoge')
#for i in range(n):
#    print(Tvote[i],Avote[i])
print(Tvote[n-1]+Avote[n-1])


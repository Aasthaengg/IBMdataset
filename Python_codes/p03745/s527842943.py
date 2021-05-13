import sys

read= sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
MOD = 1000000007
sys.setrecursionlimit(10**7)

#N,*A = map(int,read().split())
N = int(input())
A = list(map(int,input().split()))

#現在作ってる数列の種類を記録
# 単調増加：1
# 単調減少 ：-1
# 初期値:0
State = 0

#答え入れる
res = 1

for i in range(1,N):
    
    #A[i]はA[i-1]と比べたときの大小を記録

    #X に現在の状態を記録
    # 増加：1
    # 減少 ：-1
    # 同じ値:0
    if A[i] > A[i-1]: #大きくなった時
        X = 1 
    elif A[i] == A[i-1]: #等しい時
        X = 0
    else :# それ以外(小さくなった時)
        X = -1

    #現在の状態と作っている数列の状態が同じとき
    if X == State:
        continue
    
    #配列の種類が0の時(どちらにもなりえる)
    if  State == 0: 
        State = X #Stateが決定されるため、更新

    #現在の状態と作っている数列の状態が違い、現在の状態が0出ないとき
    if X != State  and  X != 0: 
        res += 1 
        State = 0 #数列を初期化

print(res)



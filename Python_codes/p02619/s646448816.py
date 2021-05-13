#Aの入力

D=int(input())

c = list(map(int, input().split()))

s = []#Dx26の行列
for i in range(D):
    s += [list(map(int, input().split()))]

t = [int(input()) for i in range(D)]#Aの出力 (コンテスト名　0~25) len = D

last = [0 for i in range(len(c))]#最後に行われた日

value = 0

v = []#len = 26

for i in range(D):
    value += s[i][t[i]-1]
    last[t[i]-1] = i+1
    for j in range(26):
        value -= c[j]*(i+1 - last[j])
    v += [value] 


#Bの出力
for i in range(D):
    print(v[i])
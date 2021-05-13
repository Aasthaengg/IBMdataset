a = input().split()
n = int(a[0])
q = int(a[1])

N = [] #プロセス名
T1 = [] #必要時間


for i in range(n):
    a = input().split()
    N.append(a[0])
    T1.append(int(a[1]))

t = 0 #経過時間
f = 0 #処理対象
l = len(N)-1 #最後尾

while len(N) > 0:
    if T1[f] <= q: #処理が完了する
        t += T1[f]
        if f == len(N)-1:
            print(N.pop(f), t)
            del T1[f]
            f = 0
        elif f == 0:
            print(N.pop(f), t)
            del T1[f]
            l -= 1
        else:
            print(N.pop(f), t)
            del T1[f]
        
        if len(N) == 0: break

    else: #処理が完了しない
        t += q
        T1[f] -= q

        i = N[f]
        j = T1[f]

        if f+1 == len(N): f = 0
        else: f += 1
        if l+1 == len(N): l = 0
        else: l += 1
        
        N[l] = i
        T1[l] = j

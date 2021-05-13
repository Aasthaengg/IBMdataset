n = int(input())
v = list(map(int, input().split()))

u = v[1::2] #奇数列
d = v[0::2] #偶数列

U = [0] * 100010
for i in range(len(u)): #何種類の数が何個現れるか記録
    U[u[i]] += 1
    
D = [0] * 100010
for i in range(len(d)): #何種類の数が何個現れるか記録
    D[d[i]] += 1
   
if U.index(max(U)) == D.index(max(D)): #最頻値が同じ場合
    u = sorted(U, reverse=True)
    d = sorted(D, reverse=True)
    s = n - u[1] - d[0] if u[1] > d[1] else n - u[0] - d[1]
    print(s)
    exit()
    
print(n - max(U) - max(D))

N = int(input())
K = int(input())
I = list(map(int,input().split()))
dis = 0

for i in I:
    a = i           #0からiまでの距離
    b = abs(K-i)    #Kからiまでの距離
    if a >= b:
        dis += 2 * b
    else:
        dis += 2 * a


print(dis)
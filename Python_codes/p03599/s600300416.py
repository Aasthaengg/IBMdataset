from math import gcd

A, B, C, D, E, F = map(int, input().split())

N = 0; max_SW = A*100; max_S = 0
f = F//100; a = f//A; b = f//B
cn = D // gcd(C, D)

for j in range(b+1): #Bをj杯入れる
    for i in range(a+1): #Aをi杯入れる
        if i==0 and j==0:
            continue
        elif A*i + B*j > f:
            continue
        w = (A*i + B*j) * 100 #水の量
        e = (A*i + B*j) * E #この場合において溶ける砂糖の最大値
        S = min(e, F-w) #ビーカーも考慮した砂糖を入れられる限界
        s = 0
        for ci in range(min(S//C, cn)+1):
            s = max(s, S - (S - C*ci) % D)
        if s/(w+s) > N:
            N = s/(w+s)
            max_SW = s + w
            max_S = s

print(max_SW, max_S)

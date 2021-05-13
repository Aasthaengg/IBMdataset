N = int(input())
A = list(map(int,input().split()))
num = [0 for i in range(3)]
suma = 1
mod = 10**9+7
for i in A:
    suma = (suma*num.count(i))%mod
    if num[0] == i:
        num[0] += 1
    elif num[1] == i:
        num[1] += 1
    else:
        num[2] += 1
print(suma)
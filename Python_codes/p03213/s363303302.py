N = int(input())

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i ==0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr

d = {}
for i in range(2,N+1):
    for j in factorization(i):
        if j[0] not in d:
            d[j[0]] = j[1]
        else:
            d[j[0]] += j[1]

ans = 0
#74
for k in d.keys():
    if d[k] >= 74:
        ans += 1
#2 24
c2 = 0
c24 = 0
for k in d.keys():
    if d[k] >= 2:
        c2 += 1
    if d[k] >= 24:
        c24 += 1
ans += c24*(c2-1)
#4 14 
c4 = 0
c14 = 0
for k in d.keys():
    if d[k] >= 4:
        c4 += 1
    if d[k] >= 14:
        c14 += 1
ans += c14*(c4-1)
#2 4 4
ans += c4*(c4-1)*(c2-2)//2

print(ans)
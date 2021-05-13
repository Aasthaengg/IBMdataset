def prime_factor(n):
    ass = []
    for i in range(2,int(n**0.5)+1):
        while n % i==0:
            ass.append(i)
            n = n//i
    if n != 1:
        ass.append(n)
    return ass

n = int(input())
if n == 1:
    print(0)
    exit()
dic = {}
for i in range(2,n+1):
    l = prime_factor(i)
    for x in l:
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1
a,b,c,d,e = 0,0,0,0,0
for x in dic.values():
    if x >= 74:
        e += 1
    elif x >= 24:
        d += 1
    elif x >= 14:
        c += 1
    elif x >= 4:
        b += 1
    elif x >= 2:
        a += 1
ans = e #75
ans += (d + e) * (a + b + c) + (d + e) * (d + e - 1) #25*3
ans += (d + e + c) * b + (d + e + c) * (d + e + c- 1) #15*5
f = b + c + d + e
ans += f * (f - 1) // 2 * a + f * (f - 1) * (f - 2) // 2  #5*5*3
print(ans) 
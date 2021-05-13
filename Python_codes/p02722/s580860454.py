def yakusu(x):
    ya = []
    for i in range(1,int(x**0.5)+1):
        if x % i == 0:
            ya.append(i)
            if i != x//i:
                ya.append(x //i)
    return ya

n = int(input())
l,m,ans = yakusu(n),yakusu(n-1),0
for i in range(1,len(l)):
    a = n
    while a % l[i] == 0:
        a = a // l[i]
    if (a-1) % l[i] == 0:
        ans += 1
ans += len(m)
print(ans-1)
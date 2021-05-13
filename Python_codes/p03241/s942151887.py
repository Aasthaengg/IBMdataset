N,M = map(int,input().split())

#nの約数列挙
def divisor(n):
    ass = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            ass.append(i)
            if i**2 == n:
                continue
            ass.append(n//i)
    return ass #sortされていない

div = divisor(M)
ans = 0
for d in div:
    if M//d >= N:
        ans = max(ans,d)
print(ans)
